from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# from web01 import models
from web01.models import User
from django.template import RequestContext
# Create your views here.


def index(request):
    return HttpResponse('<h1>Home views</h1>')

def show_user_list(request):
    users = User.objects.all()
    
    return render_to_response('index.html',{
        'users':users,
        })

def list_sort(request,u_field):
    print u_field
    users = User.objects.order_by(u_field)
    print users
    return render_to_response('index.html',{
        'users':users,
        })
#     return HttpResponse('ok')


def search_from(request):
    return render_to_response('search_form.html')

def search(request):
#     data = request.GET['q']
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        users = User.objects.filter(UserName=q)
#         print users
        return render_to_response('search_form.html', {'users': users})
#         return HttpResponse(user)
    else:
        return render_to_response('search_form.html',{
            'error':""
            })
        

def addUser_form(request):
    return render_to_response('userAdd.html',context_instance=RequestContext(request))


def AddUser(request):
    
    data = request.POST
    username = data.get('username')
    password = data.get('password')
    age = data.get('age')
    print username, password, age
    user = User(UserName=username,PassWord=password,Age=age)
    user.save()
    
    return render_to_response('index.html',{
        'info': username,
        })
    
    
def test(request,username):
    print username
    return HttpResponse('<h1>your name is %s <h1>' % username)
    
    

    
    