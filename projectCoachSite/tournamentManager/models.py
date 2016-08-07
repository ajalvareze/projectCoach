from django.db import models

# Create your models here.
class Team(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField('nombre', max_length=200)

class Match(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    location = models.CharField('ubicacion', max_length=200)
    date = models.DateTimeField('fecha')
    team1 = models.ForeignKey(Team, related_name='team1')
    team2 = models.ForeignKey(Team, related_name='team2' )
    result1 = models.PositiveIntegerField()
    result2 = models.PositiveIntegerField()      
    
class Tournament(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField('nombre', max_length=200)
    DFB = models.CharField(max_length=200) 
    matches = models.ManyToManyField(Match, blank=True)
