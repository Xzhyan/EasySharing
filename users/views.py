from django.shortcuts import render

# Auth, login e register
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                print('logado')

            else:
                print("Problema no login ou usuário/senha incorretos!")
        
        else:
            print('Formulário inválido!')

    else:
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form': form})
