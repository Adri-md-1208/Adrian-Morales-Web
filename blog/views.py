from django.shortcuts import render
from blog.models import Post

def blog(request):
    """
    Blog where posting news or comments
    """
    posts = Post.objects.all()

    return render(request, "blog/blog.html", {'posts': posts})


