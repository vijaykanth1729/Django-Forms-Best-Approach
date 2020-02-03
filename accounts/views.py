from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            # if remember_me:
            #     request.session.set_expiry(1209600)
            return redirect('books:list')
        else:
            messages.error(request, 'Bad username or password Try again!!')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('books:list')

def register_view(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #print(form) gives all the raw data in the html representation..
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email=email, password=password)
            messages.success(request, f'Thanks for registering with us {user.username}')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})


#




