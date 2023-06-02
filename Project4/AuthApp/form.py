from AuthApp.models import CustomUser,EmployDetail
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('email','phone')


class EmployForm(forms.ModelForm):
    class Meta:
        model = EmployDetail
        fields = '__all__'