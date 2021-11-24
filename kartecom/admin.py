from django.contrib import admin

# Register your models here.
from kartecom.models import Session, Todo, Idea

admin.site.register(Idea)
admin.site.register(Todo)