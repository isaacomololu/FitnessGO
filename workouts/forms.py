from django import forms
from .models import CustomWorkout

class CustomWorkoutForm(forms.ModelForm):
    class Meta:
        model = CustomWorkout
        fields = ['name', 'description', 'exercises']