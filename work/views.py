from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required

@login_required()
def workouts(request):
    response = requests.get('https://exercisedb.p.rapidapi.com/exercises?category=chest', headers={'x-rapidapi-key': '6423e39cd6msh44a05dc5213ccc0p153801jsn39d457166d6f'})
    workouts = response.json()
    print(response.text)
    return render(request, 'workout.html', {'workouts':workouts})