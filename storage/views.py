from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse, FileResponse
from django.shortcuts import get_list_or_404
from django.db import IntegrityError

# Models
from .models import Archive

# Usos especificos
from io import BytesIO
import zipfile

User = get_user_model()

# ------- Funções -------

def upload_files(request):
    file_list = request.FILES.getlist('file_list')
    file_owner = request.user

    if not file_list:
        messages.error(request, "Nenhum arquivo foi selecionado para upload!")
        return
    
    for file_obj in file_list:
        size_bytes = file_obj.size
        size_mb = round(size_bytes / (1024 * 1024), 2)

        try:
            save_file, created = Archive.objects.update_or_create(
                archive = file_obj,
                file_name = file_obj.name,
                size = size_mb,
            )

            if created:
                save_file.owner_id = file_owner
                save_file.save()
                messages.success(request, "Arquivo(s) enviado(s) com sucesso!")
        
        except IntegrityError:
            messages.error(request, "Erro de integridade no banco de dados.")
        
        except Exception as e:
            messages.error(request, f"Erro: {e}")

def download_files(request):
    file_list = request.POST.getlist('file-checkbox')

    if not file_list:
        messages.error(request, "Por favor, selecione um ou mais arquivos!")
        return False

    file_objs = Archive.objects.filter(id__in=file_list)

    if not file_objs.exists():
        messages.error(request, "O arquivo não foi encontrado no banco de dados!")
        return False
    
    # Verifica se é apenas um ou são mais arquivos pra download.
    if len(file_list) > 1:
        pass

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

def delete_files(request):
    pass    

# ------- Views -------

def actions(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    
    action = request.POST.get('action')

    if action == 'upload':
        upload_files(request)

    elif action == 'download':
        response = download_files(request)

        if isinstance(response, FileResponse):
            return response
    
    elif action == 'delete':
        pass
    
    return redirect('main')

def main_storage(request):
    """
    Pra não confundir, usei 'archive' para os arquivos listados no frotend
    e 'file_list' para a lista de arquivos que vão ser tratados como upload, delete, download e outros.
    """

    archives = Archive.objects.all()
    return render(request, 'storage/home.html', {'archives': archives})