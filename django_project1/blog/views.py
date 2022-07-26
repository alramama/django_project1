from django.shortcuts import render

from django.shortcuts import render
from .models import FilesAdmin


def home(request):
    # get all objects
    OUR_CONTEXT={'file':FilesAdmin.objects.all()}
    return render(request,'blog/home.html',OUR_CONTEXT)


import os
from django.conf import settings
from django.http import HttpResponse, Http404,request,response

def download(request, path):
    # get the download path
    download_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(download_path):
        with open(download_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(download_path)
            return response
    raise Http404
