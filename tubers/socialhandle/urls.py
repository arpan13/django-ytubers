from django.urls import path,include
from . import views

urlpatterns=[
    path('socialhandle',views.socialhandle,name="socialhandle"),
    
]