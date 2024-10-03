from django.urls import path

from settings.views import settings


urlpatterns = [
    path('',settings,name='settings')
]