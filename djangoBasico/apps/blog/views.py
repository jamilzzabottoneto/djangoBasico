from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def coments(request):
    return render(request, 'blog/comentarios.html')