from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render, redirect
from .forms import ExcelUploadForm
from django.conf import settings
import os

REQUIRED_COLUMNS = ['Tenant first name', 'Tenant last name', 'Tenant email', 'Tenant phone number', 'Tenant identification card', 'Tenant identification number']

# Create your views here.
def home(request):
    return render(request, 'home.html')

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)

            # saving columns in session to be used in the next step
            request.session['temp_data'] = df.to_json()
            # print(df.to_json())
            request.session['user_headers'] = list(df.columns)
            return redirect('map_headers')
    else:
        form = ExcelUploadForm()
    return render(request, 'upload.html', {'form': form})

def map_headers(request):

    # retrieves from the previous session,if not default to empty
    user_headers = request.session.get('user_headers', [])
    df = pd.read_json(request.session['temp_data'])

    if request.method == 'POST':
        # Build mapping from user input
        user_mapping = {}
        for sys_col in REQUIRED_COLUMNS:
            user_col = request.POST.get(sys_col)
            if user_col:
                user_mapping[user_col] = sys_col

        # Rename and validate
        df.rename(columns=user_mapping, inplace=True)
        missing_headers = [col for col in REQUIRED_COLUMNS if col not in df.columns]

        if missing_headers:
            return render(request, 'map_headers.html', {
                'user_headers': user_headers,
                'required_columns': REQUIRED_COLUMNS,
                'error': f'Missing mapped columns: {missing_headers}'
            })

        missing_rows = df[df[REQUIRED_COLUMNS].isnull().any(axis=1)]

        if not missing_rows.empty:
            missing_rows['Error'] = 'Missing required field(s)'
            error_file = os.path.join(settings.MEDIA_ROOT, 'rows_with_missing_data.xlsx')
            missing_rows.to_excel(error_file, index=True)
            return render(request, 'upload_result.html', {'error_file': 'media/rows_with_missing_data.xlsx'})
        else:
            # Accept data — you can store or process it here
            cleaned_data = os.path.join(settings.MEDIA_ROOT, 'cleaned_data.xlsx')
            df.to_excel(cleaned_data, index=False)
            return render(request, 'upload_result.html', {'success': True, 'cleaned_data':'media/cleaned_data.xlsx' })

    return render(request, 'map_headers.html', {
        'user_headers': user_headers,
        'required_columns': REQUIRED_COLUMNS
    })


