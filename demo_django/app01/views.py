from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json

# Create your views here.

def index(request):
    return render_to_response('update.html')



def Auth(request):
    print request.GET['username']
    user,passwd = request.GET['username'],request.GET['password']
    if user=='Alex' and passwd == 'alex3714':
        
        return HttpResponse("welcom user %s login our website " % user)
    else:
        return HttpResponse("username or password error ")


def menu(request):
    region_dic={
        "ShanDong":{'Liaocheng':["Dong'e",'Shenxian'],
                    'Jinnan':['Shanghe','Jiyang']
            },
        'anhui':{'anqing':['Susong','Huaining']}

        }
    
    return HttpResponse(json.dumps(region_dic))

def update(request):
    return render_to_response('update.html')