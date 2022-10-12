from . import views
from django.urls import path, include

urlpatterns = [
  
    path('get/', views.FileUploadCreateRead.as_view(
        {"get": "get_file"}), name='get_file'),
    path('get_specific_file/<int:pk>/', views.FileUploadCreateRead.as_view(
        {"get": "get_specific_file"}), name='get_specific_file'),
    path('create_single/', views.FileUploadCreateRead.as_view(
        {"post": "create_single_file"}), name='create_single_file'),
    path('create/', views.FileUploadCreateRead.as_view(
        {"post": "create_file"}), name='create_file'),
    path('edit/<int:pk>/', views.FileUploadCreateRead.as_view(
        {"put": "edit_file"}), name='edit_file'),
    path('delete/<str:uuid>/', views.FileUploadCreateRead.as_view(
        {"delete": "delete_file"}), name='delete_file'),

] 
