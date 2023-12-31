# Generated by Django 4.2.7 on 2023-11-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0014_customworkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='fitness_goal',
            field=models.CharField(choices=[('Stay Fit', 'Stay Fit'), ('Lose Weight', 'Lose Weight'), ('Build Muscle', 'Build Muscle'), ('Keep Fit', 'Keep Fit'), ('Improve Endurance', 'Improve Endurance')], default='SF', max_length=20),
        ),
    ]
