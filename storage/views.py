from django.shortcuts import render

def main_storage(request):
    return render(request, 'storage/home.html')