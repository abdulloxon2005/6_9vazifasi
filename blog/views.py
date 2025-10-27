from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    maqolalar = Post.objects.all()
    return render(request, 'blog/index.html',{'maqolalar': maqolalar})


def maqola(request, pk):
    post = Post.objects.get(id = pk)
    return render(request, 'blog/maqola.html', {"post":post})