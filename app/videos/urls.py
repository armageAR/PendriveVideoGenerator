from django.urls import path

from . import views

urlpatterns = [
    path('', views.video_list_view, name='index'),
]
