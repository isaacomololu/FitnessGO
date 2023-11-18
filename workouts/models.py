from django.db import models


class Workout(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=150)
    duration = models.PositiveIntegerField()
    duration_unit = models.CharField(
        max_length=10,
        choices=[
            ('seconds', 'Seconds'),
            ('minutes', 'Minutes'),
            ('hours', 'Hours'),
        ],
        default='minutes'
    )
    exercises = models.ManyToManyField('Exercise', related_name='workouts')  # Use string form
    completed = models.BooleanField(default=False)
    INTENSITY_LEVELS = [
        ('L', 'low'),
        ('M', 'moderate'),
        ('V', 'vigorous')
    ]
    intensity = models.CharField(
        max_length=20,
        choices=INTENSITY_LEVELS,
        default='M'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_duration_in_minutes(self):
        if self.duration_unit == 'seconds':
            return self.duration / 60
        elif self.duration_unit == 'hours':
            return self.duration * 60
        else:
            return self.duration

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.exercises.count() < 3:  
            for _ in range(3 - self.exercises.count()):
                exercise = Exercise.objects.create(name="Exercise", description="Exercise description", weight=0,
                                                   equipment_required="None", difficulty_level='M', repetitions=5,
                                                   sets=3)
                self.exercises.add(exercise)
class Exercise(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    weight = models.DecimalField(max_digits=999, decimal_places=1, null=True, blank=True)
    equipment_required = models.CharField(max_length=50, null=True, blank=True)
    DIFFICULTY_LEVELS = [
        ('VH', 'Very Hard'),
        ('H', 'Hard'),
        ('M', 'Moderate'),
        ('E', 'Easy')
    ]
    difficulty_level = models.CharField(
        max_length=20,
        choices=DIFFICULTY_LEVELS,
        default='M'
    )
    repetitions = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()

    def __str__(self):
        return self.name

