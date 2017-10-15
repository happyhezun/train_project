from django.shortcuts import render, render_to_response
from models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    return render_to_response('archive.html', {'posts':posts})
