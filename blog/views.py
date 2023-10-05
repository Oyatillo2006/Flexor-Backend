from django.shortcuts import render

from .models import Blog

def blog(request):
    data = {
        "blogs": Blog.objects.all()
    }
    return render(request, "blog.html", data)


def blog_single(request, id):
    data = {
        "blog": Blog.objects.get(id=id)
    }

    return render(request, "blog-single.html", data)