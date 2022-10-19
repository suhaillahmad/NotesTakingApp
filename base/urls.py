from turtle import update
from django.urls import path
from . import views


urlpatterns = [
    path('', views.createNotes, name="home"),
]
