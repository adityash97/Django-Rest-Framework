from atexit import register
from django.contrib import admin
from .models import Product,Base_User
# Register your models here.

admin.site.register(Product)

@admin.register(Base_User)
class Base_UserAdmin(admin.ModelAdmin):
    list_fields = ['username', 'email', 'is_staff', 'phone']
