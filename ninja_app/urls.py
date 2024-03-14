# ninja_app/urls.py

from django.urls import include, path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('eight_ball/', views.eight_ball, name='eight_ball'),  # Add this line
]


