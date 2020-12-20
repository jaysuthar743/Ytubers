from django.shortcuts import render
from .models import Slider, Team

from youtubers.models import Youtuber

# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_youtubers = Youtuber.objects.all()

    # data: all values(data) u want to pass to template
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': featured_youtubers,
        'all_youtubers': all_youtubers,
    }
    return render(request,'webpages/home.html', data)

def about(request):
    teams = Team.objects.order_by("-created_date")
    data = {
        "teams": teams
    }
    return render(request,'webpages/about.html', data)

def services(request):
    return render(request,'webpages/services.html')

def contact(request):
    return render(request,'webpages/contact.html')

