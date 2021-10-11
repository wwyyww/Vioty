from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from map.models import Cctv, Violent
import json


def main(request):
    #db 추가작업
    # url="http://openapi.seoul.go.kr:8088/6743624b646c6b323433736e6f7647/json/safeOpenCCTV_nw/1/1000/"
    # url="http://openapi.seoul.go.kr:8088/6743624b646c6b323433736e6f7647/json/safeOpenCCTV_nw/1001/1810/"

    cctv_result=[]
    # res=requests.get(url)

    # rdata=res.json()['safeOpenCCTV_nw']
    # items=rdata.get('row')

    # for result in items:
    #     cctv = Cctv()
    #     cctv.latitude = float(result['WGSXPT']) 
    #     cctv.longtitude = float(result['WGSYPT'])
    #     cctv.address = str(result['ADDR'])
    #     cctv.save()

    #     location = {
    #         'x' : result['WGSXPT'],
    #         'y' : result['WGSYPT']
    #     }
    #     cctv_result.append(location)

    
    class_object=Cctv.objects.all()

    for object in class_object:
        location = {
            'x' : object.latitude,
            'y' : object.longtitude
        }
        cctv_result.append(location)

    items = {
        'location' : cctv_result
    }

    # data=json.dumps(cctv_result)


    return render(request, 'map/main.html', items)


def camera(request):
    return render(request, 'map/camera.html')
