from django import forms

class GameForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Descrição'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Ano'}))
    foto = forms.ImageField(required=False)

    