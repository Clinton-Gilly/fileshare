from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SharedFile
import json
from django.core import serializers

def home(request):
    return render(request, 'sharing/base.html')

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        name = request.POST.get('fileName')
        password = request.POST.get('password', '')

        shared_file = SharedFile(
            name=name,
            original_name=file.name,
            file=file,
            password=password if password else None
        )
        shared_file.save()
        return JsonResponse({'status': 'success'})

def get_files(request):
    sent_files = SharedFile.objects.filter(is_received=False)
    received_files = SharedFile.objects.filter(is_received=True)
    
    sent_data = [{
        'name': f.name,
        'date': f.date_uploaded.strftime('%Y-%m-%d %H:%M'),
        'hasPassword': bool(f.password)
    } for f in sent_files]
    
    received_data = [{
        'name': f.name,
        'date': f.date_uploaded.strftime('%Y-%m-%d %H:%M'),
        'hasPassword': bool(f.password)
    } for f in received_files]

    return JsonResponse({
        'sent': sent_data,
        'received': received_data
    })