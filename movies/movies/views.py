from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import Movie

def movies(request):
    data = Movie.objects.all
    return render(request, 'movies/movies.html', { 'movies': data } )

def home(request):
    return HttpResponse("Home Page")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data} )

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404("The movie does not exist")

    movie.delete()

    return HttpResponseRedirect('/movies')

def pdf_report_create(request):
    movies = Movie.objects.all

    template_path = 'movies/pdfReport.html'
    context = {'movies': movies}

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
    