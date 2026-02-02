from django import forms

class ProfileForm(forms.Form):
    name = forms.CharField(label="Введите имя", max_length=100)
