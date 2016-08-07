from django.http import HttpResponse
from django.shortcuts import render

from .models import Tournament

def index(request):
    tournament_list = Tournament.objects.order_by('id')[:5]
    context = {'tournament_list' : tournament_list }
    return render(request, 'tournamentManager/index.html' ,context)
    
def detail(request, tournament_id):
    try:
        tournament = Tournament.objects.get(pk=tournament_id)
    except Tournament.DoesNotExist:
        raise Http404("No existe el torneo")
    return render(request, 'tournamentManager/detail.html', {'tournament': tournament})
# Create your views here.
def match(request, match_id):
    return HttpResponse(match_id)
    
def team(request, team_id):
    return HttpResponse(team_id)