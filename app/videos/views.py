from django.shortcuts import render
from .models import Video
from .forms import VideoForm


def video_list_view(request):
    queryset = Video.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "videos/list.html", context)


def video_create_view(request):
    form = VideoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VideoForm()
    context = {
        'form': form
    }
    return render(request, "videos/create.html", context)
