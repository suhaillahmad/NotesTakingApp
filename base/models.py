from distutils.command.upload import upload
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Notes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    bookmark = models.IntegerField(default=0)
    picture = models.ImageField(upload_to="media", null=True, blank=True, default = 'media/body.jpg')
    
    class Meta:
        ordering = ['-updated', '-created']
    
    
    def __str__(self):
        return self.title

class Search(models.Model):
    status = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.status
        
        
