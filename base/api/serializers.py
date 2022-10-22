from dataclasses import field
from rest_framework.serializers import ModelSerializer
from base.models import *

class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
        
class titleSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = ('id','title')