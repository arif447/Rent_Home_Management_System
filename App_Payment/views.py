from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import BankForm, CardForm, payment_choice_form

@login_required
def Payment_Choice(request):
    form = payment_choice_form()
    if request.method == 'POST':
       form = payment_choice_form(request.POST)
       if form.is_valid():
          payment_user = form.save(commit=False)
          payment_user.billing_user = request.user
          payment_user.save()
          messages.success(request, 'Successfully Complete Billing Info')

    diction = {'form': form}
    return render(request, 'App_Payment/pyment_choice.html', context=diction)


@login_required
def Card_Info(request):
    form = CardForm()
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Complete ')
    diction = {'form': form}
    return render(request, 'App_Payment/cardinfo.html', context=diction)


@login_required
def Bank_Info(request):
    form = BankForm()
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Complete ')
    diction = {'form': form}
    return render(request, 'App_Payment/bankinfo.html', context=diction)






