from django.shortcuts import render, redirect
from .models import ContactTeam
from django.contrib import messages

# Create your views here.

def contactTeam(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        details_message = request.POST['details_message']
        user_id = request.user

        contactTeam = ContactTeam(
            full_name=full_name, phone=phone, email=email, company_name=company_name, subject=subject, details_message=details_message, user_id=user_id)
        contactTeam.save()
        messages.success(request, "Your Query Has Been Sent to Our Team!!")
        return redirect("home")
        



