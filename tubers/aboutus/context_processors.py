from .models import Aboutus


def about_us(request):
    about_us=Aboutus.objects.all()
    
  
    
    return{
        "about_us":about_us[0].desc,
    }
    