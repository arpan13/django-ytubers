from django.db import models
from datetime import datetime
# Create your models here.
class ContactTuber(models.Model):
    name=models.CharField(max_length=255)
    company_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    message=models.TextField(blank=True)
    user_id=models.IntegerField(blank=True)
    created_at=models.DateTimeField(blank=True,default=datetime.now)
    
    def __str__(self):
        return self.email