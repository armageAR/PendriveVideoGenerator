from django.urls import path

from . import views

urlpatterns = [
    path('', views.VideoList.as_view(), name='video-list'),
    path('create/', views.VideoCreate.as_view(), name='video-create'),
    path('<int:pk>/', views.VideoDetail.as_view(), name='video-details'),
    path('<int:pk>/update/', views.VideoUpdate.as_view(), name='video-update'),
    path('<int:pk>/delete/', views.VideoDelete.as_view(), name='video-delete'),
]
