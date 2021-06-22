from django.db import models

# Create your models here.
class SocialHandle(models.Model):
    email=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    facebook_link=models.CharField(max_length=255,blank=True)
    instagram_link=models.CharField(max_length=255,blank=True)
    twitter_link=models.CharField(max_length=255,blank=True)
    youtube_link=models.CharField(max_length=255,blank=True)
    copyright_date=models.CharField(max_length=255,blank=True)
    
    
    def __str__(self):
        return self.email