from django.shortcuts import render
from .models import DietPlan

def diet(request):
    diet_plans = DietPlan.objects.all()
    return render(request, 'diet.html', {'diet_plans':diet_plans})

