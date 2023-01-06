from django.contrib import admin
from movielist_app.models import Movie,Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)