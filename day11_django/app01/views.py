from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
data = ['hanxin', 'wangfanghao', 'alex']


def index(request):
    return HttpResponse('<h1>app01.views</h1>')

def List(request, id):
    if id:
        id = int(id)
        if id >= 0 and id < len(data):
            result = data[id]
            return HttpResponse(result)
    
    result = '<br/>'.join(data)
    return HttpResponse('<h1>' + result +'</h1>')