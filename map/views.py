from django.shortcuts import render

import requests

# Create your views here.
    

def main(request):
    url="http://openapi.seoul.go.kr:8088/6743624b646c6b323433736e6f7647/json/safeOpenCCTV_nw/1/5/"

    cctv_result=[]
    res=requests.get(url)
    rdata=res.json()['safeOpenCCTV_nw']
    items=rdata.get('row')

    for result in items:
        context = {
            'WGSXPT' : result['WGSXPT']
        }
        cctv_result.append(context)

    print(cctv_result)


    return render(request, 'map/main.html', context)

