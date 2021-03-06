from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import post

def post_create(request):
    return HttpResponse("<h1> CREATE</h1>")

def post_detail(request, id=None):
    instance = get_object_or_404(post,id=id)
    context = {
            "title" : instance.title,
            "instance" : instance,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = post.objects.all()
    context = {
            "object_list" : queryset,
        "title": "List"
        }
    return render(request, "index.html",context)

def post_update(request):
    return HttpResponse("<h1> UPDATE </h1>")

def post_delete(request):
    return HttpResponse("<h1> DELETE </h1>")