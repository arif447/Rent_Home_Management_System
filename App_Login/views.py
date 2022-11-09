from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# import form and model

from App_Login.models import CreateUser, user_registration
from App_Add_Flat.models import Category, Add_Flat
from App_Login.forms import CreatUserForm, LoginForm, User_Registration_Form

# Messages
from django.contrib import messages
# Create your views here.
def signup(request):
    form = CreatUserForm()
    register = False
    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            register = True
            messages.success(request, 'Successfully create a account')
            return HttpResponseRedirect(reverse('App_Login:login'))
    diction = {'form': form}
    return render(request, 'App_Login/signup.html', context=diction)


def login_user(request):
      form = LoginForm(request.POST or None)
      if request.method == 'POST':
         if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                messages.success(request, 'Successfully Login')
                return HttpResponseRedirect(reverse('home'))
            elif user is not None and user.is_renter:
                login(request, user)
                messages.success(request, 'Successfully Login')
                return HttpResponseRedirect(reverse('home'))
            elif user is not None and user.is_owner:
                login(request, user)
                messages.success(request, 'Successfully Login')
                return HttpResponseRedirect(reverse('home'))
      return render(request, 'App_Login/login.html', context={'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.warning(request, 'you are logout')
    return HttpResponseRedirect(reverse('App_Login:login'))


""""
@login_required
def registrationform(request):
    form = User_Registration_Form()
    if request.method == 'POST':
        form = User_Registration_Form(request.POST, request.FILES)
        if form.is_valid():
            user_object = form.save(commit=False)
            user_object.user = request.user
            user_object.save()
            messages.success(request, 'Successfully registration')
            return HttpResponseRedirect(reverse('home'))
    diction = {'form': form}
    return render(request, 'App_Login/registration.html', context=diction)

"""

@login_required
def User_profile(request):
    return render(request, 'App_Login/user_profile.html', context={})


def searchbar(request):
    if request.method == 'GET':
        search = request.GET.get('query', '')
        result = Add_Flat.objects.filter(Bedroom__icontains=search)
    return render(request, 'App_Login/search.html', context={'result': result, 'search': search})

