from django.urls import path

#let's reuse the django login view
from django.contrib.auth import views as auth_views

from spareApp import views

urlpatterns = [
    #pages urls
   
    path('', views.index, name= 'index'),
    path('home2/', views.home2, name= 'home2'),
    #home page
    path('home', views.home, name= 'home'),
    path('home/<int:product_id>', views.product_detail, name= 'product_detail'),
    
    #Reciept url
    #
    path('receipt/', views.receipt, name= 'receipt'),
    
    path('receipt/<int:receipt_id>', views.receipt_detail, name= 'receipt_detail'),
    
    
    #All sales made
    path('all_sales/', views.all_sales, name= 'all_sales'),
    path('issue_item/<str:pk>', views.issue_item, name= 'issue_item'),
    
    #Add to stock
    path('add_to_stock/<str:pk>', views.add_to_stock, name= 'add_to_stock'),
    
    #delet functionality view
    path('delete/<int:product_id>', views.delete_product, name= 'delete_product'),
    
    #Login path 
    path('login/', auth_views.LoginView.as_view(template_name = 'spare/login.html'), name= 'login'),
    
    path('logout/', auth_views.LogoutView.as_view(template_name = 'spare/index.html'), name= 'logout'),
    
    
]