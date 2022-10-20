from django.contrib import admin
from .models import Notes
from .models import Category
# Register your models here.

admin.site.register(Notes)
admin.site.register(Category)
