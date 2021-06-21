from django.contrib import admin
from .models import ContactTuber
# Register your models here.

class CYadmin(admin.ModelAdmin):
    list_display=('name','email','phone','subject')


admin.site.register(ContactTuber,CYadmin)