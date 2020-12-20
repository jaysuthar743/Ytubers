
from django.shortcuts import render
from myheader.models import Header
from myfooter.models import Footer

# Create your views here.

def myheader(request):
    header = Header.objects.all()
    return {
        'header':header
    }


def myfooter(request):
    footer = Footer.objects.all()
    return {
        'footer' : footer
    }