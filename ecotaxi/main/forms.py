from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Почтовый адрес', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-input'}),
        #     'password1': forms.TextInput(attrs={'class': 'form-input'}),
        #     'password2': forms.TextInput(attrs={'class': 'form-input'}),
        # }
        
    # def clean_password1(self):
    #     password1 = self.cleaned_data['password1']
    #     if len(password1) < 9:
    #         raise ValidationError('Введите минимум 9 символов')
    #
    #     return password1
    