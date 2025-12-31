from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': "",
            'placeholder': "Digite seu nome de usuário..."
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "",
            'placeholder': "Digite sua senha de acesso..."
        })
    )
