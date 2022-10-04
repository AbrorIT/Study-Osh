from django.shortcuts import render 
from apps.settings.models import Setting, About, AboutImage


# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    context = {
        'home' : home,
    }
    return render(request, 'index', context)

    
    
def about_us(request):
    home = Setting.objects.latest('id')
    about = About.objects.latest('id')
    image = AboutImage.objects.all().order_by('-id')
    context = {
        'home' : home,
        'about' : about,
        'image' : image,
    }
    return render(request, 'about',  context)