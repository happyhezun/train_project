from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
# Create your views here.

data = {
        "ShanDong":{'Liaocheng':["Dong'e",'Shenxian'],
                    'Jinnan':['Shanghe','Jiyang']
            },
        'anhui':{'anqing':['Susong','Huaining'],
                 
                 },
         "ShanDong":{'Liaocheng':["Dong'e",'Shenxian'],
                    'Jinnan':['Shanghe','Jiyang']
            },
        
    }

def index(request):
    return render_to_response('index.html')

def GetProvince(request):
    result = data.keys()
    
    return HttpResponse(json.dumps(result))


def GetCity(request):
    getData = request.GET
    provinceID = getData.get('Id')
    result = data.values()
    temp = type(provinceID)
    result2 = result[int(provinceID)]
    result3 = result2.keys()
   
    return HttpResponse(json.dumps(result3))


def GetCounty(request):
    getData = request.GET
    provinceId = getData.get('proId')
    cityId = getData.get('cityId')
    result = data.values()
    result2 = result[int(provinceId)]
    result3 = result2.values()
    result4 = result3[int(cityId)]

    return HttpResponse(json.dumps(result4))
    
    