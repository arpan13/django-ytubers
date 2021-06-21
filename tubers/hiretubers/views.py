from django.shortcuts import redirect, render
from .models import HireTuber
from django.contrib import messages,auth
# Create your views here.

#     first_name=models.CharField(max_length=255)
#     last_name=models.CharField(max_length=255)
#     email=models.CharField(max_length=255)
#     city=models.CharField(max_length=255)
#     state=models.CharField(max_length=255)
#     phone=models.CharField(max_length=255)
#     message=models.TextField(blank=True)
#     user_id=models.IntegerField(blank=True)
#     tuber_id=models.IntegerField()
#     tuber_name=models.CharField(max_length=255)

def hiretuber(request):
    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        city=request.POST["city"]
        state=request.POST["state"]
        phone=request.POST["phone"]
        message=request.POST["message"]
        tuber_id=request.POST["tuber_id"]
        user_id=request.POST["user_id"]
        tuber_name=request.POST["tuber_name"]
        
        
        #TODO: do all sanitization
        
        hiretuber = HireTuber(
            first_name=first_name,
            last_name=last_name,
            email=email,
            city=city,
            state=state,
            phone=phone,
            message=message,
            user_id=user_id,
            tuber_id=tuber_id,
            tuber_name=tuber_name
            )
        
        hiretuber.save()
        messages.success(request,"Thanks for reaching out")
        return redirect("youtubers")
        
        