from django.shortcuts import render, get_object_or_404, redirect
from .models import FileUploadModel
from .forms import FileUploadForm


def upload_list(request):
    return render(request, 'upload_list.html', {
        'upload_list': FileUploadModel.objects.all()
    })


def upload_form(request, pk):
    upload = get_object_or_404(FileUploadModel, pk=pk)

    if request.method == 'POST':
        form = FileUploadForm(
            instance=upload, data=request.POST, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect('upload-list')
    else:
        form = FileUploadForm(instance=upload)

    return render(request, 'upload_form.html', {
        'form': form
    })