from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import *
from .serializers import *

@api_view(['GET'])
def MyNotes(request):
        Note = Notes.objects.all()

        searchResult = request.GET.get('searchResult') or ''

        if searchResult:
            Note = Note.filter(title__icontains=searchResult)

        serializer = titleSerializer(Note, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
def viewNote(request,pk):
    Note = Notes.objects.get(id=pk)
    
    serializer = NotesSerializer(instance=Note, many= False)
    return Response(serializer.data)

@api_view(['POST'])
def createNotes(request):
   serializer = NotesSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
   
   return Response(serializer.data)

@api_view(['GET','PUT'])
def updateNotes(request, pk):
    Note = Notes.objects.get(id=pk)
    serializer = NotesSerializer(instance=Note, data=request.data)
    if serializer.is_valid():
       serializer.save()
   
    return Response(serializer.data)

@api_view(['GET','DELETE'])
def deleteNotes(request, pk):
    Note = Notes.objects.get(id=pk)
    Note.delete()
    
    return Response("Deleted Successfully")
