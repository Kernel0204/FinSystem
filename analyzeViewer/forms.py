from django import forms
from .models import *



class userAddForm(forms.ModelForm):
    class Meta:
        model = users
        exclude = ()




class groupAddForm(forms.ModelForm):
    class Meta:
        model = groups
        exclude = ()