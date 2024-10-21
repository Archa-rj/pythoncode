from django import forms
from .models import FeedBack

class FeedBackFromUser(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'