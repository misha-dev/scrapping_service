from django import forms
from scrapper.models import City, Language, Jobs


class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), to_field_name='slug', required=False, widget=forms.Select(attrs={'class': 'form-control'}), label='Город')
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(), to_field_name='slug', required=False, widget=forms.Select(attrs={'class': 'form-control'}), label='Язык Программирования')
