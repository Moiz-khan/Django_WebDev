from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="shopHome"),
    path('about/', views.about, name="aboutUs"),
    path('contact/', views.contact, name= "contactUs"),
    path('tracker/', views.tracking, name= "tracking"),
    path('search/', views.search, name= "searching"),
    path('productview/<int:myid>', views.product_view, name= "product_view"),
    path('checkout/', views.checkout, name= "checkout"),

]
