from django.shortcuts import redirect, render
from django.contrib.auth.models import User  , auth
from django.contrib import messages


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            return redirect ('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name =  request.POST['last_name']
        User_name= request.POST['User_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password==confirmpassword:
            if User.objects.filter(username=User_name).exists():
                messages.info(request,'user already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=User_name,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()

        return redirect('/')

    else:
        
        return render(request, 'register.html')
# Create your views here.
