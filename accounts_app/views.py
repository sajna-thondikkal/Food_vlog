from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"username already taken...")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist..")
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                print("user created")
        else:
            print("error... not created..")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,"registration.html")

def login_logout(request):
    return render(request,'login.html')