from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid user")
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        use=request.POST['username']
        first= request.POST['first_name']
        last = request.POST['last_name']
        eml = request.POST['email']
        pas= request.POST['password']
        conpass = request.POST['password1']
        if pas == conpass:
           if User.objects.filter(username=use).exists():
               messages.info(request, "username taken")
               return redirect('register')
           elif User.objects.filter(email=eml).exists():
               messages.info(request,"email taken")
               return redirect('register')
           else:
               user = User.objects.create_user(username=use, first_name=first, last_name=last, email=eml, password=pas)
               user.save();
               return redirect('login')

        else:
           messages.info(request, "password not match")
           return redirect('register')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
