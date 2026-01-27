from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': "w-full max-w-sm bg-stone-900 hover:bg-stone-800 rounded-sm p-2 shadow-md outline-none text-sm",
            'placeholder': "Usuário",
            "autocomplete": "username",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "w-full max-w-sm bg-stone-900 hover:bg-stone-800 rounded-md p-2 shadow-md outline-none text-sm",
            'placeholder': "Senha",
            "autocomplete": "current-password",
        })
    )
