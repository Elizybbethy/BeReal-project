from django.urls import path
from spareApp import views

urlpatterns = [
    # path('index/', views.index, name= 'index'),
    path('', views.index, name= 'index'),
]