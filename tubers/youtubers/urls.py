from django.urls import path,include

from . import views

urlpatterns=[
    path('',views.youtubers,name="youtubers"),
    path('<int:id>',views.youtubers_details,name="youtubers_details"),
    path('search',views.search,name="search"),
]