from django.shortcuts import render
from django.shortcuts import render , redirect
from .models import Post , Comment
from .forms import CommentForm



# Create your views here.

def post_list (request):

    data = Post.objects.all()

    context = {
        'object_list' : data
    }
    return render(request,'posts/post_list.html',context)



def post_detail (request,slug) :
    data = Post.objects.get(slug = slug)
    comments = Comment.objects.filter(post=data)
    if request.method == 'POST' :
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.post = data
            myform.save()
    else :
        form = CommentForm()
    context = {
        'post' : data,
        'comments': comments,
        'form' : form,
    }
    return render (request , 'posts/post_detail.html' , context)

