#coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from app01.models import *
# Create your views here.
data = ['hanxin', 'wangfanghao', 'alex']


def index(request):
    return HttpResponse('<h1>app01.views</h1>')
'''
def List(request, id):
    if id:
        id = int(id)
        if id >= 0 and id < len(data):
            result = data[id]
            return HttpResponse(result)
    
    result = '<br/>'.join(data)
    return HttpResponse('<h1>' + result +'</h1>')

def Model(request):

    p = ColorDic(ColorName='yellw')
    p.save()
    p.ColorName='orege'
    p.save()

# 修改
#     model = ColorDic.objects.filter(id=1).update(ColorName='綠色')
#     提取
#     model = ColorDic.objects.get(id=1)
#     模糊查詢
#     model = ColorDic.objects.filter(ColorName__contains="白")
#     model = ColorDic.objects.filter(ColorName__contains="色")[1:3]
    model = ColorDic.objects.values('ColorName')
    return HttpResponse(model)    '''
    
    
def Model(request):
    return render_to_response('model.html', {'title':'first web'})

def ModelMut(request):
    names = ['張無忌','周止若','張三風']
    return render_to_response('model.html',{'names': names})
    