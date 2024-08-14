from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment, NewsLetter, Like, TestComment

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {"blogs": blogs})

def detail(request, model_name, pk):
    model = None
    if model_name == 'blog':
        model = get_object_or_404(Blog, pk=pk)
    context = {'model': model}
    return render(request, 'details.html', context)

def comment(request):
    comments = TestComment.objects.all()
    if request.method == 'POST':
        data = request.POST['comment']
        send = TestComment(comment=data)
        send.save()
    return render(request, 'comment.html', {"comments": comments})

def update_comment(request, pk):
    comment = get_object_or_404(TestComment, pk=pk)
    if request.method == 'POST':
        new_comment = request.POST['comment']
        comment.comment = new_comment 
        comment.save()  
        return redirect('comment')
    return render(request, 'update_comment.html', {"comment": comment})


def delete_comment(request, pk):
    comment = get_object_or_404(TestComment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment')
    return render(request, 'confirm_delete.html', {"comment": comment})

