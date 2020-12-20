from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from hiretubers.models import Hireubers

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #  this user is 
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.warning(request, "You Are Logged In")
            return redirect('dashboard')

        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('login')

    return render(request, "accounts/login.html")

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.warning(request, "Username Already Exist")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, "Email Already Exist")
                    return redirect('register')
                else:
                    user  = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    user.save()
                    messages.success(request, "Account Created Successfully")
                    return redirect('login')
        else:
            messages.warning(request, "Password Does Not Match!!")
            return redirect('register')
    return render(request, "accounts/register.html")


def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    current_user = request.user
    current_user_id = current_user.id
    hired_tubers = Hireubers.objects.all().filter(user_id=current_user_id)
    data = {
       "hired_tubers" : hired_tubers
    }
    return render(request, "accounts/dashboard.html", data)


