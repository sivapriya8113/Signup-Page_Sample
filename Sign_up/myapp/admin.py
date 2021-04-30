from django.contrib import admin

# Register your models here.

from .models import register

admin.site.register(register)