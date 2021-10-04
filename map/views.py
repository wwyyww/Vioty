from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from map.models import Cctv, Violent


# Create your views here.
# def map(request):
#     url="http://openapi.seoul.go.kr:8088/6743624b646c6b323433736e6f7647/json/safeOpenCCTV_nw/1/5/"

#     res=requests.get(url)
#     rdata=res.json()
#     print(rdata)
    
#     context = {
#         'rdata': rdata
#     }
    
#     return render(request, 'main.html', context)

def main(request):
    url="http://openapi.seoul.go.kr:8088/6743624b646c6b323433736e6f7647/json/safeOpenCCTV_nw/1/5/"

    cctv_result=[]
    res=requests.get(url)

    rdata=res.json()['safeOpenCCTV_nw']
    items=rdata.get('row')

    for result in items:
        # cctv = Cctv()
        # cctv.latitude = float(result['WGSXPT']) 
        # cctv.longtitude = float(result['WGSYPT'])
        # cctv.save()

        location = {
            'x' : result['WGSXPT'],
            'y' : result['WGSYPT']
        }
        cctv_result.append(location)

    
    class_object=Cctv.objects.all()

    items = {
        'location' : cctv_result,
        'class_object' : class_object
    }

    

    


    return render(request, 'map/main.html', items)
