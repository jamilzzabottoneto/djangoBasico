from django.shortcuts import render
from djangoBasico.data import posts


# Create your views here.
def index(request):
    context = {
        'text':'Essa é a view do BLOG do projeto',
        'title': 'Esse é o titulo do Blog',
        'posts': posts,
        }
    return render(request, 'blog/index.html', context)

def coments(request):
    context = {
        'text':'Essa é a view do BLOG/Comentarios do projeto',
        'title': 'Esse é o titulo do Comentarios',
        }
    return render(request, 'blog/comentarios.html', context)

def post(request, id):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)