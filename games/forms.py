from django import forms

class GameForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.Textarea()
    date = forms.DateField()
    foto = forms.ImageField(required=False)
    