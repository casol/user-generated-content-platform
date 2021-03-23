from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('<slug:custom_url>/', views.content_detail, name='content_detail'),
    path('add/upload/', views.content_upload, name='content_upload'),
]
