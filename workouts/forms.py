from django import forms
from .models import Workout

class CustomizeWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'exercises', 'duration', 'intensity']

class WorkoutForm(forms.ModelForm):
    pass