from django import forms
from .models import UserDetails

class LoginModelForm(forms.ModelForm):
    class Meta:
        model=UserDetails
        fields ='__all__'
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter your name'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'age':forms.NumberInput(attrs={'placeholder':'Enter your age'})
        }
        