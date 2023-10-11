from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import *


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        exclude = ["user"]


class BorrowedForm(ModelForm):
    class Meta:
        model = Borrowed_items
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
