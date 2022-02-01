from django.contrib import admin
from .models import Artcile
# Register your models here.

@admin.register(Artcile)
class AtricleAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','date','email']


