import os
from django.shortcuts import render, redirect
from base.forms import NotesForm
from .models import Notes
from .filters import OrderFilter


# Create your views here.



def MyNotes(request):
    
    Note = Notes.objects.all()

    
    myFilter = OrderFilter(request.GET, queryset=Note)
    Note = myFilter.qs
    
    searchResult = request.GET.get('search-area') or ''
    
    if searchResult:
        Note = Note.filter(title__icontains=searchResult)
    
    context = {'Note' : Note, 'myFilter': myFilter}
    return render(request, 'base/home.html', context)

def createNotes(request):
    form = NotesForm
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('MyNotes')
    
    context = {'form' : form}
    return render(request, 'base/create_note.html', context)

def updateNotes(request, pk):
    Note = Notes.objects.get(id=pk)
    form = NotesForm(instance=Note)
    
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES ,instance=Note)
        if form.is_valid():
            form.save()
            return redirect('MyNotes')
    
    context = {'form':form}
    return render(request, 'base/create_note.html', context)


def deleteNotes(request, pk):
    Note = Notes.objects.get(id=pk)
    if request.method == 'POST':
        Note.delete()
        return redirect('MyNotes')
    
    return render(request, 'base/delete.html', {'obj':Note})

def viewNote(request, pk):
    Note = Notes.objects.get(id=pk)
    
    return render(request, 'base/view_note.html', {'obj':Note})

def addBookmark(request, pk):
    Note = Notes.objects.get(id=pk)
    
    Note.bookmark = 1
    Note.save()
    
    Note = Notes.objects.all()
    return redirect('MyNotes')


def deleteBookmark(request,pk):
    Note = Notes.objects.get(id=pk)
    
    Note.bookmark = 0
    Note.save()
    
    Note = Notes.objects.all()
    return redirect('MyNotes')

def viewbookmarks(request):
    Note = Notes.objects.all()
    
    
    myFilter = OrderFilter(request.GET, queryset=Note)
    Note = myFilter.qs
    
    searchResult = request.GET.get('search-area') or ''
    
    if searchResult:
        Note = Note.filter(title__icontains=searchResult)
    
    context = {'Note' : Note, 'myFilter': myFilter}
    return render(request, 'base/bookmarks.html', context)

    
        
