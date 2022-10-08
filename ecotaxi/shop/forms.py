from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class AddProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = ShopProducts
        fields = ['title', 'slug', 'description_small', 'description_big', 'photo', 'date',
                  'code', 'price', 'manufacturer', 'material', 'size', 'color', 'cat']
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-input'}),
            'description_small': forms.Textarea(attrs = {'cols': 60, 'rows': 3}),
            'description_big': forms.Textarea(attrs = {'cols': 60, 'rows': 10})
        }
        
