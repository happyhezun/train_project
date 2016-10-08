from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
data = ['hanxin', 'wangfanghao', 'alex']


def List(request):
    
    result = '<br/>'.join(data)
    return HttpResponse('<h1>' + result +'</h1>')