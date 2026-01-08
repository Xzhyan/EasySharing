from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

# Models
from .models import Archive

# Usados no tratamento dos arquivos
import io, zipfile
from django.http import HttpResponse, FileResponse
from django.shortcuts import get_object_or_404

# User model
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
                file_name = file_obj,
                size = size_mb,
            )

            if created:
                save_file.owner_id = file_owner
                save_file.save()
                messages.success(request, "Arquivo(s) enviado(s) com sucesso!")
        
        except Exception as e:
            messages.error(request, e)

def download_files(request):
    file_list = request.POST.getlist('file-checkbox')

    if not file_list:
        messages.error(request, "Por favor, selecione um ou mais arquivos!")
        return
    
    file_objs = Archive.objects.filter(id__in=file_list)

    try:
        file_obj = file_objs[0]
        file_path = file_obj.archive.path
        file_response = open(file_path, 'rb')
        return FileResponse(file_response, as_attachment=True, filename=file_obj.archive.name)

    except FileNotFoundError:
        raise messages.error(request, "Arquivo(s) inexistente(s)!")

# ------- Views -------

def main_storage(request):
    """
    Pra não confundir, usei 'archive' para os arquivos listados no frotend
    e 'file_list' para a lista de arquivos que vão ser tratados como upload, delete, download e outros.
    """
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'upload_form':
            upload_files(request)

        elif form_type == 'download_form':
            download_files(request)

        return redirect('main')

    archives = Archive.objects.all()
    return render(request, 'storage/home.html', {'archives': archives})