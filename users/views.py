from django.shortcuts import render, redirect

# Auth, login e register
from django.contrib.auth import authenticate, login, get_user_model, logout
from .forms import LoginForm

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
                print("O usuário informado não existe!")
                
            else:
                user = authenticate(request, username=username, password=password)
                
                if user is not None:
                    login(request, user)
                    print('Logado com sucesso!')
                    return redirect('storage/main')

                else:
                    print("Problema no login ou usuário/senha incorretos!")
        
        else:
            print('Formulário inválido!')

    else:
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user-login')
