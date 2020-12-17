from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm): #Create a new class called RegisterForm, that inherits from UserCreationForm
    email = forms.EmailField() ##add a new attribute to the class called email

    class Meta: #Creating a class inside this class called Meta, allows us to change the attributes of the parent class 
        model = User #This means the form will make changes to the user model whenever 
        fields = ["username","email","password1","password2"] # If we're going to add extra fields (eg email that we've added above), we need to list all the fields we want shown on the form here (including the built in ones like username and password 1 / 2)