from django.shortcuts import render, redirect
from .models import Hireubers
from django.contrib import messages

# Create your views here.

"""
first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=255)
    message = models.TextField(max_length=300)
    user_id = models.IntegerField(blank=True)

"""
def hiretubers(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        #  to do
        hiretubers = Hireubers(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name, email=email, city=city, state=state, phone=phone, message=message, user_id=user_id)
        hiretubers.save()
        messages.success(request, "Thanks for reaching out")
        return redirect('youtubers')

