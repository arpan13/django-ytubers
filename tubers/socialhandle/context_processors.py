from .models import SocialHandle
from django.shortcuts import render,get_object_or_404
def social_context(request):
    socials=get_object_or_404(SocialHandle,pk=1)

    
    return {
        "email":socials.email,
        "phone":socials.phone
        }
        