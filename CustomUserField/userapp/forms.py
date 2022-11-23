from django.contrib.auth.forms import  UserCreationForm
from django import forms

# change this to get get user model
# from django.contrib.auth.models import User

# the above User is not our user now

from django.contrib.auth import get_user_model # this will give the actual user model

User = get_user_model() # This gives swapped user module do this everywhere

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2']

