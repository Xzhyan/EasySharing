from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required

from .utils.custom_decorators import check_permission

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


def create_new_user(request, redirect_to, msg_text):
    """Função criar um usuário, usada tanto na view user_register quanto na view user_create"""
    form = RegisterForm(request.POST)

    if form.is_valid():
        User.objects.create_user(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            role = 'default'
        )
        messages.success(request, msg_text)
        return redirect(redirect_to)
    
    else:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, error)


def user_register(request):
    if request.method == 'POST':
        redirect_to = 'user-login'
        msg_text = "Acesso solicitado com sucesso."
        create_new_user(request, redirect_to, msg_text)

    form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, "Você saiu do sistema!")
    return redirect('user-login')


@login_required(login_url='user-login')
@check_permission('control')
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário modificado com sucesso!")
            return redirect('control')
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
        
    else:
        form = UserEditForm(instance=user)

    context = {
        'user': user,
        'form': form
    }

    return render(request, 'users/edit.html', context)


@login_required(login_url='user-login')
@check_permission('control')
def user_delete(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        
        try:
            user.delete()
        
        except Exception as e:
            messages.error(request, f"Erro: {e}")

        messages.success(request, 'Usuário removido com sucesso.')

    return redirect('control')


@login_required(login_url='user-login')
@check_permission('control')
def user_create(request):
    if request.method == 'POST':
        redirect_to = 'control'
        msg_text = "Novo usuário criado com sucesso."
        create_new_user(request, redirect_to, msg_text)

    form = RegisterForm()

    return render(request, 'users/create.html', {'form': form})

