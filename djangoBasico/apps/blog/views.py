from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'text':'Essa é a view do BLOG do projeto',
        'title': 'Esse é o titulo do Blog',
        }
    return render(request, 'blog/index.html', context)

def coments(request):
    context = {
        'text':'Essa é a view do BLOG/Comentarios do projeto',
        'title': 'Esse é o titulo do Comentarios',
        }
    return render(request, 'blog/comentarios.html', context)