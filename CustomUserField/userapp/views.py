from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from userapp.forms import CreateUserForm    
from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Created.." )
            return loginUser(request)
        messages.error(request, 'user validation failed')
        
    return render(request, 'register.html', {'form':form})


def loginUser(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.info(request, "username or password is incorrect..")
    context = {}
    return render(request, 'login.html', context)

def logOut(request):
    logout(request)
    return home(request)

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def profile(request):
    context={}
    return render(request, 'profile.html', context)










