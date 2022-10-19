from turtle import update
from django.urls import path
from . import views


urlpatterns = [
    path('', views.MyNotes, name="MyNotes"),
    path('create-note/', views.createNotes, name="createNotes")
]
