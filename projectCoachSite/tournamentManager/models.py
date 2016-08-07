from django.db import models

# Create your models here.
class Team(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField('nombre', max_length=200)
    
    def __str__(self):
        return self.name

class Match(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    location = models.CharField('ubicacion', max_length=200)
    date = models.DateTimeField('fecha')
    team1 = models.ForeignKey(Team, related_name='team1')
    team2 = models.ForeignKey(Team, related_name='team2' )
    result1 = models.PositiveIntegerField()
    result2 = models.PositiveIntegerField()      
    
    def __str__(self):
        return str(self.date) + " " + self.location + " " + " " + self.team1.name + " vs " + self.team2.name

    
class Tournament(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField('nombre', max_length=200)
    DFB = models.CharField(max_length=200) 
    matches = models.ManyToManyField(Match, blank=True)
    
    def __str__(self):
        return self.name