from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model

# Models
from .models import Archive

# Usados no tratamento dos arquivos
import io, zipfile
from django.http import HttpResponse, FileResponse

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
                return
        
        except Exception as e:
            messages.error(request, e)
            return

def download_files(request):
    file_list = request.POST.getlist('file-checkbox')

    if not file_list:
        messages.error(request, "Nenhum arquivo foi selecionado!")
        return

    if len(file_list) > 1:
        buffer = io.BytesID()

        try:
            with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                for file_obj in file_list:
                    save_file = file_obj.file_name or f"file_{file_obj.id}.ext"
                    zip_file.write(file_obj.file.path, arcname=save_file)

        except Exception as e:
            print(e)

# ------- Views -------

def main_storage(request):
    """
    Pra não confundir, usei 'archive' para os arquivos listados no frotend
    e 'file_list' para a lista de arquivos que vão ser tratados como upload, delete, download e outros.
    """

    archives = Archive.objects.all()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'upload_form':
            upload_files(request)

        elif form_type == 'download_form':
            download_files(request)

    return render(request, 'storage/home.html', {'archives': archives})