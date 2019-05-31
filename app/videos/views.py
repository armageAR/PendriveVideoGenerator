from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)


from django.urls import reverse_lazy

from .models import Video
from .forms import VideoForm


class VideoList(ListView):
    model = Video
    template_name = 'videos/list.html'
    # context_object_name =


class VideoDetail(DetailView):
    model = Video
    template_name = 'videos/details.html'


class VideoCreate(CreateView):
    model = Video
    success_url = reverse_lazy('video-list')
    fields = ['title', 'category', 'videoFile']
    template_name = "videos/form.html"


class VideoUpdate(UpdateView):
    model = Video
    success_url = reverse_lazy('video-list')
    fields = ['title', 'category', 'videoFile']
    template_name = "videos/form.html"


class VideoDelete(DeleteView):
    model = Video
    success_url = reverse_lazy('video-list')
    template_name = "videos/delete.html"
