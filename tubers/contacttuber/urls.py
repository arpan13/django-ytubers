from django.urls import path,include
from . import views

urlpatterns=[
    path("contacttuber",views.contacttuber,name="contacttuber"),
    
]