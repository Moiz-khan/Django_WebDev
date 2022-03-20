from django.forms import ModelForm
#importing forms
from django.contrib.auth.forms import UserCreationForm
#importing user model in django admin
from django.contrib.auth.models import User
from django import forms



# from .models import Order

# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields  = "__all__"

#inherit with user creation Form
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields  = ['first_name','last_name', 'username', 'email', 'password1', 'password2','fullname']