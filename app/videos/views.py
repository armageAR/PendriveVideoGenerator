from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from .forms import VideoForm


def video_list_view(request):
    queryset = Video.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "videos/list.html", context)


def video_create_view(request):
    template = "videos/create.html"
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video-list')
    else:
        form = VideoForm()

    context = {'form': form}
    return render(request, template, context)


def video_update_view(request, id=id):
    template = "videos/create.html"
    obj = get_object_or_404(Video, id=id)

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('video-list')
        else:
            # form invalid
            return redirect('video-list')
    else:
        form = VideoForm(None, instance=obj)
    context = {'form': form}
    return render(request, template, context)

def video_delete_view(request, id):
    obj = get_object_or_404(Video, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('video-list')
    context = {
        "object": obj
    }
    return render(request, "videos/delete.html", context)

def video_detail_view(request, id):
    obj = get_object_or_404(Video, id=id)
    context = {
        "object": obj
    }
    return render(request, "videos/details.html", context)