from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse, FileResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Models
from .models import Archive, Folder

# Usos especificos
from io import BytesIO
import zipfile

User = get_user_model()


# ------- Funções -------

def upload_files(request, folder_id):
    file_list = request.FILES.getlist('upload_list')
    file_owner = request.user
    
    folder = get_object_or_404(Folder, id=folder_id)

    if not file_list:
        messages.error(request, "Nenhum arquivo foi selecionado para upload!")
        return
    
    for file_obj in file_list:
        try:
            save_file = Archive.objects.update_or_create(
                file_name = file_obj,
                defaults={
                    'archive': file_obj,
                    'owner_id': file_owner,
                    'folder_id': folder,
                    'size': file_obj.size
                }
            )

        except IntegrityError:
            messages.error(request, "Erro de integridade no banco de dados.")
            return
        
        except Exception as e:
            messages.error(request, f"Erro: {e}")
            return

    messages.success(request, "Arquivo(s) enviado(s) com sucesso!")


def download_files(request):
    file_list = request.POST.getlist('selected')

    if not file_list:
        messages.error(request, "Por favor, selecione um ou mais arquivos!")
        return

    file_objs = Archive.objects.filter(id__in=file_list)

    if not file_objs.exists():
        messages.error(request, "Arquivo(s) inexistente(s) no armazenamento!")
        return

    # Verifica se é apenas um ou são mais arquivos pra download.
    # Se for mais de um ele cria um .zip para baixar os arquivos.
    if len(file_list) > 1:
        buffer = BytesIO()

        with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for file_obj in file_objs:
                file_obj_path = file_obj.archive.path
                zip_name = file_obj.archive.name.split('/')[-1]
                zip_file.write(file_obj_path, zip_name)

        buffer.seek(0)

        response = HttpResponse(
            buffer,
            content_type='application/zip'
        )
        response['Content-Disposition'] = 'attachment; filename="easysharing.zip"'
        return response

    else:
        try:
            file_obj = file_objs[0]
            file_obj_path = file_obj.archive.path

            response = FileResponse(
                open(file_obj_path, 'rb'),
                as_attachment=True,
                filename=file_obj.file_name
            )
            return response
    
        except Exception as e:
            messages.error(request, f"Erro: {e}")
            return


def delete_files(request):
    file_list = request.POST.getlist('selected')

    if not file_list:
        messages.error(request, "Por favor, selecione um ou mais arquivos!")
        return
    
    file_objs = Archive.objects.filter(id__in=file_list)
    
    for file_obj in file_objs:
        try:
            file_obj.archive.delete(save=False)
            file_obj.delete()
        
        except Exception as e:
            messages.error(request, "Erro: {e}")
            return

    messages.success(request, "Arquivo(s) deletado(s) com sucesso!")
    return


# ------- Views -------

@login_required(login_url='user-login')
def control(request):
    users = User.objects.all()

    actives = []
    inactives = []

    for user in users:
        if user.is_active:
            actives.append(user)
        else:
            inactives.append(user)

    context = {
        'actives': actives,
        'inactives': inactives
    }
    
    return render(request, 'storage/control.html', context)


@login_required(login_url='user-login')
def actions(request, folder_id):
    if request.method != 'POST':
        return HttpResponse(status=405)
    
    action = request.POST.get('action')

    if action == 'upload':
        upload_files(request, folder_id)

    elif action == 'download':
        response = download_files(request)

        if response:
            return response

    elif action == 'delete':
        delete_files(request)

    return redirect('main', folder_id=folder_id)


@login_required(login_url='user-login')
def main_page(request, folder_id):
    """
    Pra não confundir, usei 'archive' para os arquivos listados no frotend
    e 'file_list' para a lista de arquivos que vão ser tratados como upload, delete, download e outros.
    """

    folder = get_object_or_404(Folder, id=folder_id)
    archives = Archive.objects.filter(folder_id=folder_id)

    context = {
        'folder': folder,
        'archives': archives
    }

    return render(request, 'storage/main.html', context)


@login_required(login_url='user-login')
def storage(request):
    if request.method == 'POST':
        user = request.user
        folder_name = request.POST.get('folder_name')
        folder_path = f'{user.username}'

        if Folder.objects.filter(folder_name=folder_name).exists():
            messages.error(request, "Essa pasta já existe.")

        else:
            Folder.objects.create(
                folder_name = folder_name,
                folder_path = folder_path,
                owner_id = user
            )

            messages.success(request, "Pasta criada com sucesso!")

    folders = Folder.objects.all()

    return render(request, 'storage/storage.html', {'folders': folders})
