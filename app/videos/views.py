from django.shortcuts import render, redirect
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
