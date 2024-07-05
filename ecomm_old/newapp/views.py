from django.shortcuts import render,redirect
from newapp.models import User as Myuser
from newapp.forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
# Create your views here.
def index(request):
    form=SignupForm()
    return render(request,"index.html",{'user':User,'form':form})
    

def signup(request):
    
    if request.method=="POST":
        form=User(request.POST)
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        
        if form.is_valid():
            try:
                form.save()
                return redirect('/') 
            except:
                pass

    else:
        form=User()
    return render(request,"login.html",{'form':form})  

def signupStore(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if form.is_valid():
            user = User.objects.create_user(username=name,password=password,email=email)
            user.save()
            return redirect('/') 

def login(request):
    if request.user.is_authenticate:
        return redirect('/')
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/signin')
    else:
        return render(request,"login.html")

        

          