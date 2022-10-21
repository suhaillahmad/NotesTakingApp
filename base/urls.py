from turtle import update
from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.MyNotes, name="MyNotes"),
    path('create-note/', views.createNotes, name="createNotes"),
    path('update-note/<str:pk>/', views.updateNotes, name="updateNotes"),
    path('delete-note/<str:pk>/', views.deleteNotes, name="deleteNotes"),
    path('note/<str:pk>/', views.viewNote, name="viewNote"),
    path('bookmark/<str:pk>/',views.addBookmark, name="addBookmark"),
    path('deletebookmark/<str:pk>/',views.deleteBookmark, name="deleteBookmark"),
    path('viewbookmarks/',views.viewbookmarks, name="viewbookmarks")
]
