from django.shortcuts import render

# Models
from .models import Archive

# ------- Funções -------

def upload_files(file_list):
    if not file_list:
        print("Não tem nenhum arquivo")
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
                save_file.owner = None
                save_file.save()
        
        except Exception as e:
            print(e)
            return

# ------- Views -------

def main_storage(request):
    """
    Pra não confundir, o usei 'archive' para os arquivos que seram listados no frotend,
    e 'file_list' pra lista de arquivos que vão ser tratador 'upload, delete, download'.
    """

    archives = Archive.objects.all()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'upload_form':
            file_list = request.FILES.getlist('file_list')
            upload_files(file_list)

    return render(request, 'storage/home.html', {'archives': archives})