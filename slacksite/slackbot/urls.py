from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.handle_slack_post, name='Posting'),
    url(r'^leaderboard/$', views.leaderboard, name='Leaderboard'),
]
