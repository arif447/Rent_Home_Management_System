from django import forms
from .models import *


class BankForm(forms.ModelForm):
    class Meta:
        model = BankInfo
        fields = '__all__'


class CardForm(forms.ModelForm):
    class Meta:
        model = CreditCardInfo
        fields = '__all__'


class payment_choice_form(forms.ModelForm):
    class Meta:
        model = BillingInfo
        fields = ['payment_method']
