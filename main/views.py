from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Settings, Servise

# Create your views here.
def index(request):
    posts = Post.objects.filter(enabled=True)

    setting = Settings.objects.filter(enabled=True).first()

    servises = Servise.objects.filter(enabled=True)

    # return render(request, "main/index.html", {'posts': posts})
    return render(request,
                  context={'posts': posts, 'setting': setting, 'servises': servises},
                  template_name="main/index.html")
