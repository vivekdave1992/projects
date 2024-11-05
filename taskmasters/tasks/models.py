from django.db import models

# Create your models here

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    team_or_single = models.CharField(max_length=10, choices=[('Team', 'Team'), ('Single', 'Single')])
    num_participants = models.IntegerField()
    items_used = models.CharField(max_length=200)
    time_needed = models.CharField(max_length=100)
    theme = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    def __str__(self):
        return self.name


    
