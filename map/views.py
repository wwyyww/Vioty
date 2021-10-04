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

    res=requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    for i in soup.find_all('row'):
        rows.append({"stop_no": i.stop_no.string,
                     "stop_nm": i.stop_nm.string,
                     "xcode": i.xcode.string,
                     "ycode": i.ycode.string})

    rdata=res.json()
    print(rdata)
    # items=rdata.get('row')
    
    # print(items)
    
    context = {
        'rdata': rdata
    }
    

    return render(request, 'map/main.html')

