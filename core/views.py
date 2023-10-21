from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['passsword2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, "Email already taken")
                return redirect('signup')

            elif User.objects.filter(userame = username).exists():
                messages.info(request, "Username already taken")
                return redirect('signup')                
            else:
                user = User.objects.create_user(username=username, email=email, password = password)
                user.save()
        else:   
            messages.info(request, "Passwords do not match")
            return redirect('signup')
    
    else:
        return render(request, 'signup.html')