from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout
from .forms import CustomizeWorkoutForm
from django.contrib.auth.decorators import login_required

@login_required()
def workouts(request, workout_id=None):
    fitness_goal = request.user.profile.fitness_goal
    recommended_workouts = Workout.objects.filter(profile=request.user.profile, profile__fitness_goal=fitness_goal)

    if workout_id:
        workout = get_object_or_404(Workout, pk=workout_id)
        if request.method == 'POST':
            form = CustomizeWorkoutForm(request.POST, instance=workout)
            if form.is_valid():
                customized_workout = form.save(commit=False)
                customized_workout.user = request.user
                customized_workout.save()
                return redirect(to='dashboard')
        else:
            form = CustomizeWorkoutForm(instance=workout)
        return render(request, 'customize_workouts', {'form': form, 'recommended_workouts': recommended_workouts})
    return render(request, 'workout.html', {'recommended_workouts': recommended_workouts})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def create_workout(request):
    return render(request, 'create_workout')

def customize_workouts(request):
    return render(request, 'customize_workouts')
