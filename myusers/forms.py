from django.forms import ModelForm
from myusers.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","phone","password1","password2","role"]
