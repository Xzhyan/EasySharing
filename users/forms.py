from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': "bg-stone-900 hover:bg-stone-800 rounded-md p-2 shadow-md outline-none",
            'placeholder': "Digite seu nome de usuário..."
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "bg-stone-900 hover:bg-stone-800 rounded-md p-2 shadow-md outline-none",
            'placeholder': "Digite sua senha de acesso..."
        })
    )
