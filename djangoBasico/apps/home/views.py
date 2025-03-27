from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'text':'Essa é a home do projeto',
        'title': 'Esse é o titulo da Home',
        }
    return render(request, 'home/index.html', context)