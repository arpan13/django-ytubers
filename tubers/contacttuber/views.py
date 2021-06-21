from django.contrib import messages
from django.shortcuts import redirect, render
from .models import ContactTuber
# Create your views here.


    # name=models.CharField(max_length=255)
    # company_name=models.CharField(max_length=255)
    # email=models.CharField(max_length=255)
    # phone=models.CharField(max_length=255)
    # message=models.TextField(blank=True)
    # user_id=models.IntegerField(blank=True)
    # created_at=models.DateTimeField(blank=True,default=datetime.now)
    
    
def contacttuber(request):
    
    if request.method == "POST":
        name=request.POST["name"]
        company_name=request.POST["company_name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]
        subject=request.POST["subject"],
        user_id=request.POST["user_id"]
        
        
        
        contacttuber=ContactTuber(
            name=name,
            company_name=company_name,
            email=email,
            phone=phone,
            message=message,
            subject=subject,
            user_id=user_id
            )
        
        
        contacttuber.save()
        messages.success(request,'Query Submitted We will get in touch')
        return redirect("youtubers")