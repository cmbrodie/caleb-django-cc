from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 5,
            'title': 'Jaws',
            'year': 1557
        },
        {
            'id': 7,
            'title': 'Alien',
            'year': 1979
        },
        {
            'id': 17,
            'title': 'The Dark Knight',
            'year': 2008
        }
        ]
}
def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home Page")
