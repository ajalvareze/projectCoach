from django.conf.urls import url

from . import views

app_name = 'tournamentManager'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^<tournament_id>[0-9]+/$', views.detail, name='detail'),
    url(r'^<match_id>[0-9]+/$', views.match, name='match'),
    url(r'^<team_id>[0-9]+/$', views.team, name='team'),
]