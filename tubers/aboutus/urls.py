from django.urls import path,include

from . import views

urlpatterns=[
    path('aboutus',views.aboutus,name="aboutus"),
    
]