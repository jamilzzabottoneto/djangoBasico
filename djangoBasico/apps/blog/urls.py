from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #path('post/', views.index, name='home'),
    path('', views.index, name='home'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('comentarios/', views.coments, name='coments')
]
