from django.urls import path
from App_Payment import views
app_name = 'App_Payment'

urlpatterns = [
    path('payment_choice/', views.Payment_Choice, name='payment'),
    path('card/', views.Card_Info, name='card_info'),
    path('bank/', views.Bank_Info, name='bank_info'),

]

