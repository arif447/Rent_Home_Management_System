from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
# Import views
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# import models and Form
from App_Add_Flat.models import Add_Flat
from App_Add_Flat.forms import Add_FlatForm

# Messages
from django.contrib import messages


# model import
from App_Login.models import CreateUser
from App_Flat_Booking.models import Booking

# Create your views here.


class Home(ListView):
    context_object_name = 'object_list'
    model = Add_Flat
    template_name = 'home.html'


def add_flat(request):
    form = Add_FlatForm()
    if request.method == 'POST':
        form = Add_FlatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Add  Flat')
            return HttpResponseRedirect(reverse('home'))
    diction = {'form': form}
    return render(request, 'App_Add_Flat/add_flat.html', context=diction)


class product_Details(LoginRequiredMixin, DetailView):
    context_object_name = 'details'
    model = Add_Flat
    template_name = 'App_Add_Flat/flat_details.html'


class Update_Flat(UpdateView, LoginRequiredMixin):
    model = Add_Flat
    fields = '__all__'
    template_name = 'App_Add_Flat/update_flat.html'
    success_url = reverse_lazy('home')


class delete_flat(DeleteView, LoginRequiredMixin):
    model = Add_Flat
    template_name = 'App_Add_Flat/delete_flat.html'
    success_url = reverse_lazy('home')


def category_type(request):
    return render(request, 'App_Add_Flat/category.html', context={})