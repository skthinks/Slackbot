from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.posting, name='Posting'),
    url(r'^leaderboard$', views.leaderboard, name='Leaderboard'),
    url(r'^leaderboard/weekly$', views.leaderboard, name='Weekly'),
    url(r'^leaderboard/monthly$', views.leaderboard, name='Monthly')
]
