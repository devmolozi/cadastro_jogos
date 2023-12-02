from django import forms
from models import Game

class GameForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    date = forms.CharField()

