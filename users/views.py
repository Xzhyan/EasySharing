from django.shortcuts import render, redirect
from django.contrib import messages

# Auth, login e register
from django.contrib.auth import authenticate, login, get_user_model, logout
from .forms import LoginForm, RegisterForm

User = get_user_model()

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user_obj = User.objects.get(username=username)

            except User.DoesNotExist:
                user_obj = None
            
            if user_obj == None:
                messages.info(request, "O usuário informado não existe!")
                
            else:
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logado com sucesso!")
                    return redirect('storage/main')

                else:
                    messages.error(request, "Problema no login ou usuário/senha incorretos!")
        
        else:
            print('Formulário inválido!')
    else:
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']

            if password != repeat_password:
                messages.error(request, "As senhas não coicidem!")

            elif User.objects.filter(username=username).exists():
                messages.error(request, "Este nome de usuário já existe!")
            
            else:
                user = User.objects.create_user(username=username, password=password, role='default')
                messages.success(request, "Acesso solicitado com sucesso!")
                return redirect('user-login')

        else:
            print('Formulário inválido!')

    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "Você saiu do sistema!")
    return redirect('user-login')
