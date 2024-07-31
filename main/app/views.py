from django.shortcuts import render
# Create your views here.
from .models import Blog, Comment, NewsLetter, Like

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})
