from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
# Create your views here.


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Incorrect Username or Password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password Does Not Exist')
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'An error has occured during registration! Please try again or contact our support team.')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def uploadPaper(request):
    context = {}
    return render(request, 'base/upload_paper.html', context)


def papers(request):
    context = {}
    return render(request, 'base/papers.html', context)

def speakers(request):
    context = {}
    return render(request, 'base/speakers.html', context)

def reservations(request):
    context = {}
    return render(request, 'base/reservations.html', context)

def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def userProfilePage(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'base/profile.html', context)

