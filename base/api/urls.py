from django.urls import path
from . import views


urlpatterns = [
    path('', views.MyNotes, name="MyNotes"),
    path('create-note/',views.createNotes, name="createNotes"),
    path('update-note/<str:pk>/', views.updateNotes, name="updateNotes"),
    path('delete-note/<str:pk>/', views.deleteNotes, name="deleteNotes"),
    path('note/<str:pk>/', views.viewNote, name="viewNote"),
]