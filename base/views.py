from django.shortcuts import render, redirect
from base.forms import NotesForm
from .models import Notes
# Create your views here.



def MyNotes(request):
    
    Note = Notes.objects.all()
    context = {'Note' : Note}
    return render(request, 'base/home.html', context)

def createNotes(request):
    
    form = NotesForm
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MyNotes')
    
    context = {'form' : form}
    return render(request, 'base/create_note.html', context)
