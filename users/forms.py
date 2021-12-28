#imports
from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

#Class that inherits from our other form inorder to add email option
class UserRegistForm(UserCreationForm):
    email= forms.EmailField(required=False) #don't require it
    class Meta:
        model=User
        fields=['username', 'email', 'password1','password2'] #fields shown in order

#Update User Model (email, username)
class UpdateUserForm(forms.ModelForm):
    email=forms.EmailField(required=False) #don't require user to update email when updating

    class Meta:

        model=User
        fields= ['username', 'email']

#Update profile pic
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']

