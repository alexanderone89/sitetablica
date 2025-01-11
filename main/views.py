from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.filter(enabled=True)

    return render(request, context={'posts': posts} ,template_name="main/index.html")
