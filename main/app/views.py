from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from .models import *

def home(request):
    blogs = Blog.objects.all()
    comments = Comment.objects.all()
    dictionaries = {'blogs': blogs, 'comments': comments}
    return render(request, 'index.html', dictionaries)

def detail(request, model_name, pk):
    model = None
    comments = Comment.objects.all()
    if model_name == 'blog':
        model = get_object_or_404(Blog, pk=pk)
    # context = {'model': model, 'comments': comments}
    context = {'model': model}
    return render(request, 'blog.html', context)

def comment(request):
    comment = TestComment.objects.all()
    if request.method == 'POST':
        data = request.POST.get('comment')
        send = TestComment(comment=data)
        send.save()
    return render(request, 'blog.html', {'comments': comment})

def update_comment(request, pk):
    comments = get_object_or_404(TestComment, pk=pk)
    if request.method == 'POST':
        new_comment = request.POST.get('comment')

        if new_comment:  # Ensure the comment is not empty
            comments.comment = new_comment
            comments.save()
            return redirect('comment')
        else:
            # Handle the case where the comment is empty
            error_message = "Comment cannot be empty."
            return render(request, 'update.html', {"comments": comments, "error_message": error_message})

    return render(request, 'update.html', {"comments": comments})
