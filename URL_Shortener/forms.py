from .models import ShortenedURL
from django import forms

class CreateShortenedURL(forms.ModelForm):
    
    class Meta:

        model = ShortenedURL
        fields = {'originalURL'}
        widgets = {'originalURL': forms.TextInput(attrs = {'class': 'form-control'})}