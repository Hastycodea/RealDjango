from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic.base import View
from wkhtmltopdf.views import PDFTemplateResponse
from django.views.generic import TemplateView
from django_weasyprint import WeasyTemplateResponseMixin

# Create your views here.
def home(request):
    return HttpResponse("This is the homepage")

def my_listings(request):
    return render(request, 'my_listings.html')

def render_pdf_view(request):
    template_path = 'my_listings.html'
    context = {}

    # Create a Django response object, and set content type to PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html,
       dest=response,
    #    link_callback=link_callback,  # defined above
    )

    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response

def download_pdf(request):
    template_path = 'my_listings.html'
    context = {}

    # Create a Django response object, and set content type to PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html,
       dest=response,
    #    link_callback=link_callback,  # defined above
    )

    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response

class MyPDFView(View):
    template='my_listings.html'

    def get(self, request):
        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename="hello.pdf",
                                       show_content_in_browser=True,
                                       cmd_options={'margin-top': 50,},
                                       )
        return response

class MyPDFDownload(View):
    template='my_listings.html'

    def get(self, request):
        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename="hello.pdf",
                                       show_content_in_browser=False,
                                       cmd_options={'margin-top': 50,},
                                       )
        return response
    
# class MyPDFView(WeasyTemplateResponseMixin, TemplateView):
#     template_name = 'my_listings.html'
#     pdf_filename = 'my_document.pdf'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data'] = "Some data for the template"
#         return context