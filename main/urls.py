from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('accuweather/', accuweather),
    path('openweather/', openweather),
]
