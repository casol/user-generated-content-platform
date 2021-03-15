from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('<int:pk>/', views.content_detail, name='content_detail'),
]
