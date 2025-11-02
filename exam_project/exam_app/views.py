from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def films(request):
    movies = [
        {'title': 'Interstellar', 'rating': 10.0},
        {'title': 'Dark Night', 'rating': 10.0},
        {'title': 'Oppenheimer', 'rating': 7.5},
    ]
    return render(request, 'films.html', {'movies': movies})
