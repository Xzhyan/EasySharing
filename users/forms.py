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

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Um usuário com o mesmo nome já existe.")
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat = cleaned_data.get('repeat_password')

        if password and repeat and password != repeat:
            raise forms.ValidationError("As senha não coincidem.")


class UserEditForm(forms.ModelForm):
    def clean_username(self):
        """Valida se o nome não vai repetir"""

        # Novo nome de usuário
        username = self.cleaned_data.get('username')

        # Nome de usuário atual
        current_user = self.instance

        if current_user.pk and current_user.username == username:
            return username
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Um usuário com o mesmo nome já existe.")
    
        return username


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
