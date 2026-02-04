from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

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

class RegisterForm(forms.Form):
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
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "w-full max-w-sm bg-stone-900 hover:bg-stone-800 rounded-md p-2 shadow-md outline-none text-sm",
            'placeholder': "Repita a senha",
            "autocomplete": "current-password",
        })
    )

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'role', 'is_active', 'is_admin']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "w-full max-w-sm bg-stone-900 hover:bg-stone-800 rounded-md p-2 shadow-md outline-none text-sm",
            }),
            'role': forms.Select(attrs={
                'class': "w-full max-w-sm bg-stone-900 hover:bg-stone-800 rounded-md p-2 shadow-md outline-none text-sm"
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': "cursor-pointer scale-160 translate-y-[2px] accent-green-700"
            }),
            'is_admin': forms.CheckboxInput(attrs={
                'class': "cursor-pointer scale-160 translate-y-[2px] accent-green-700"
            })
        }