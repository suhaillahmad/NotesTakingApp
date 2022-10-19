from django.shortcuts import render
from .models import Notes
# Create your views here.



def createNotes(request):
    
    Note = Notes.objects.all()
    context = {'Note' : Note}
    return render(request, 'base/home.html', context)