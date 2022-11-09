from django.urls import path
from App_Add_Flat import views

app_name = 'App_Add_Flat'

urlpatterns = [
    path('addflat/', views.add_flat, name='add_flat'),
    path('details/<pk>/', views.product_Details.as_view(), name='product_details'),
    path('update/<pk>/', views.Update_Flat.as_view(), name='update_flat'),
    path('delete/<pk>/', views.delete_flat.as_view(), name='delete_flat'),
    path('category_type/', views.category_type, name='category_type'),
]
