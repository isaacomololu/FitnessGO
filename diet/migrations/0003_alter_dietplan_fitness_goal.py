# Generated by Django 4.2.7 on 2023-11-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0002_alter_dietplan_fitness_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietplan',
            name='fitness_goal',
            field=models.CharField(choices=[('SF', 'Stay Fit'), ('LW', 'Lose Weight'), ('BM', 'Build Muscle'), ('KF', 'Keep Fit'), ('IE', 'Improve Endurance')], default='SF', max_length=20),
        ),
    ]
