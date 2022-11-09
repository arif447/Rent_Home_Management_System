from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse
# import models
from App_Add_Flat.models import Add_Flat
from App_Flat_Booking.models import Booking

from App_Login.forms import User_Registration_Form

# Authentication
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Import Views
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


@login_required
def My_flat(request, pk):
    flat = get_object_or_404(Add_Flat, pk=pk)
    Booking.objects.get_or_create(info_flat=flat, renter=request.user)
    form = User_Registration_Form()
    if request.method == 'POST':
        form = User_Registration_Form(request.POST, request.FILES)
        if form.is_valid():
           user_object = form.save(commit=False)
           user_object.user = request.user
           user_object.save()
           messages.success(request, 'Successfully registration')
           return HttpResponseRedirect(reverse('App_Login:user_profile'))
    diction = {'form': form}
    return render(request, 'App_Login/registration.html', context=diction)


@login_required
def Flat_Info(request):
    obj = Booking.objects.get(renter=request.user)
    diction = {'obj': obj}
    return render(request, 'App_Flat_Booking/flat_info.html', context=diction)


class Renters_List(ListView, LoginRequiredMixin):
    context_object_name = 'object_list'
    model = Booking
    template_name = 'App_Flat_Booking/renter_list.html'
