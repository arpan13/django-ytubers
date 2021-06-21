from django.contrib import admin
from .models import HireTuber
from django.utils.html import format_html
# Register your models here.

class HYadmin(admin.ModelAdmin):
    list_display=('email','phone','tuber_name','city','state')



admin.site.register(HireTuber,HYadmin)