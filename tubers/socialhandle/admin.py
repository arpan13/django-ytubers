from django.contrib import admin
from .models import SocialHandle
# Register your models here.

class SHadmin(admin.ModelAdmin):
    list_display=(
        "email",
        "phone",
        "facebook_link",
        "instagram_link",
        "twitter_link",
        "youtube_link",
        "copyright_date",
        )



admin.site.register(SocialHandle,SHadmin)