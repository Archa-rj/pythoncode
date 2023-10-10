from django import forms
from .models import Cartoon

class CartoonForm(forms.ModelForm):
    class Meta:
        model=Cartoon
        fields=['name','char','desc','img']