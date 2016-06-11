
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'slack/', include('slackbot.urls')),    
    url(r'^admin/', admin.site.urls),
]
