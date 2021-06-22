from django.shortcuts import get_object_or_404, render
from .models import Youtuber
from socialhandle.models import SocialHandle
# Create your views here.

def youtubers(request):
    
    socials=get_object_or_404(SocialHandle,pk=1)
    
   
    tubers= Youtuber.objects.order_by("-created_date")
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()
    
    
    
    # if 'keyword' in request.GET:
    #     keyword = request.GET['keyword']
    #     if keyword:
    #         tubers = tubers.filter(description__icontains=keyword)
            
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
            
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)
    
    
    data={
        'tubers':tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
        "email":socials.email,
        "phone":socials.phone
        
    }
    
    return render(request, 'youtubers/youtubers.html',data)

def youtubers_details(request,id):
    tuber = get_object_or_404(Youtuber,pk=id)
    socials=get_object_or_404(SocialHandle,pk=1)
    
    data = {
        "tuber":tuber,
        "email":socials.email,
        "phone":socials.phone
    }
    return render(request, 'youtubers/youtuber_detail.html',data)

def search(request):
    tubers = Youtuber.objects.order_by("-created_date")
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()
    socials=get_object_or_404(SocialHandle,pk=1)
    
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)
            
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
    
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)
            
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category)
    
    data={
        'tubers':tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search':category_search,
        "email":socials.email,
        "phone":socials.phone
        
    }
    
    return render(request, 'youtubers/search.html',data)


