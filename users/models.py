from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=True)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,  # Make this field optional
    )

    FITNESS_GOALS_CHOICES = [
        ('SF', 'Stay Fit'),
        ('LW', 'Lose Weight'),
        ('BM', 'Build Muscle'),
        ('KF', 'Keep Fit'),
        ('IE', 'Improve Endurance'),
    ]

    fitness_goal = models.CharField(
        max_length=20,
        choices=FITNESS_GOALS_CHOICES,
        default='SF'
    )
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.user.username






