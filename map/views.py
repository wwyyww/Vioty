from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

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
        location = {
            'x' : result['WGSXPT'],
            'y' : result['WGSYPT']
        }
        cctv_result.append(location)

    items = {
        'location' : cctv_result
    }

    print(items)

    return render(request, 'map/main.html', items)

