from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('create/', views.create, name='create' ),
    path('add_book/', views.add_book, name='add_book' ),
    path('delete/<id>/', views.delete, name='delete' ),
    path('edit/<id>/', views.edit, name='edit' ),
    path('update/<id>/', views.update, name='update' ),
    path('api/get/', views.api_get, name='get' ),
    path('api/post/', views.api_post, name='post' ),

]
