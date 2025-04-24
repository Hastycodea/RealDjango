from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies' : [
        {
            'id': 5,
            'title': "Django Unchained",
            'year': 2014
        },
        {
            'id': 6,
            'title': "The Dark Knight",
            'year': 2008
        },
        {
            'id': 7,
            'title': "Inception",
            'year': 2010
        }
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data )

def home(request):
    return HttpResponse("Home Page")