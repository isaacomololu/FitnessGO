from django.urls import path
from .views import workouts, dashboard

urlpatterns = [
    path('workouts/', workouts, name='workouts'),
    path('dashboard', dashboard, name='dashboard'),
]