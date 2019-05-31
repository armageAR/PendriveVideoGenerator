from django.shortcuts import render
from .models import Video


def video_list_view(request):
    queryset = Video.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "videos/list.html", context)
