from django.http import HttpRequest, Http404
from django.shortcuts import render
from djangoBasico.data import posts
from typing import Any

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

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

        if found_post is None:
            raise Http404("Post não existe")

    context = {
        'post': found_post,
        'title': found_post['title'],
    }
    return render(request, 'blog/post.html', context)