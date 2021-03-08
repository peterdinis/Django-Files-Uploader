from django.shortcuts import render
from .forms import UploadForm

def uploadFile(request):
    if request.method == "POST":
        fl = UploadForm(request.POST, request.FILES)
        if fl.is_valid():
            fl.save()
    else:
        fl = UploadForm()

    return render(request, 'files/index.html', {
        'fl': fl,
    })