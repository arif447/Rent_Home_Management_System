from django.urls import path
from App_Flat_Booking import views
app_name = 'App_Flat_Booking'

urlpatterns = [
    path('my_flat/<pk>/', views.My_flat, name='my_flat'),
    path('flatinfo/', views.Flat_Info, name='flat_info'),
    path('renter_list/', views.Renters_List.as_view(), name='renters_list'),

]
