from django.urls import path

from . import views

urlpatterns = [
    path('', views.video_list_view, name='video-list'),
    path('create/', views.video_create_view, name='video-create'),
    path('<int:id>/update/', views.video_update_view, name='video-update'),
]
