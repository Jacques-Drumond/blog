from django.shortcuts import render
from .models import Posts
# Create your views here.

def index(request):
    postagem = Posts.objects.all()
    return render(request, 'index.html', {'postagem':postagem})

def posts(request, pk):
    post = Posts.objects.get(id=pk)
    return render(request, 'post.html', {'postagem':post})