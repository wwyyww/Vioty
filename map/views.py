from django.shortcuts import render

import requests

# Create your views here.
    

def main(request):
    url="http://openapi.seoul.go.kr:8088/6743624b646c6b323433736e6f7647/json/safeOpenCCTV_nw/1/5/"

    res=requests.get(url)
    rdata=res.json()
    print(rdata)
    
    context = {
        'rdata': rdata
    }
    return render(request, 'map/main.html', context)

