from django.contrib.admin import forms
from django.forms import ModelForm, TextInput, models, DateTimeInput

from main.models import Car, News


class LimelightForm(ModelForm):
    class Meta:
        model = Car
        fields = ['id', 'img', 'model', 'marka', 'year', 'price', 'color']

        widgets = {
            "model": TextInput(attrs={
                'placeholder': 'Модель'
            }),
            "marka": TextInput(attrs={
                'placeholder': 'Марка'
            }),
            "year": TextInput(attrs={
                'placeholder': 'Год'
            }),
            "price": TextInput(attrs={
                'placeholder': 'Цена'
            }),
            "color": TextInput(attrs={
                'placeholder': 'Цвет'
            }),
        }


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['image', 'title', 'data', 'anons']

        widgets = {
            "title": TextInput(attrs={
                'placeholder': 'Тема новости'
            }),
            "data": TextInput(attrs={
            }),
            "anons": TextInput(attrs={
                'placeholder': 'Анонс новости'
            })
        }