
from django.contrib import admin
from django.urls import path, include

from landing.views import home

urlpatterns = [
    path('', home, name='home'),
    path('api/', include('api.urls')),
]
 