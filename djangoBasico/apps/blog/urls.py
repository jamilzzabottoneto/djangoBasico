from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    path('comentarios/', views.coments, name='coments')
]
