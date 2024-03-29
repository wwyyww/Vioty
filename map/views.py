from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from map.models import Cctv,  User
import bcrypt
from django.contrib import auth

def sub_map(request):
    url="http://openapi.seoul.go.kr:8088/6743624b646c6b323433736e6f7647/json/safeOpenCCTV_nw/1001/1810/"

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


    return render(request, 'map/main_new/sub_map.html', items)



def camera(request):
    return render(request, 'map/camera.html')

def login(request):
    if request.method=="POST":
        loginid=request.POST['ID']
        loginpwd=request.POST['PW']
        request.session['loginOk'] = False
        if User.objects.filter(id=loginid).exists():
            loginuser = User.objects.get(id = loginid)
            if bcrypt.checkpw(loginpwd.encode('utf-8'), loginuser.password.encode('utf-8')) :
                request.session['loginOK'] = True
                context ={
                    "userid" : loginid,
                    "result" : "로그인 성공"
                }
                return render(request, 'map/main_new.html', context)
                print("로그인 성공")
            else :
                request.session['loginOK'] = True
                context ={
                    "result" : "로그인 실패"
                }
                print("실패1")
        else :
            request.session['loginOK'] = True
            context ={
                "result" : "로그인 실패"
            }
            print("실패2")

    return render(request, 'map/login.html')

def signup(request):
    if request.method=="POST":
        if request.POST['PW1'] == request.POST['PW2']:
            id=request.POST['ID']
            password=request.POST['PW1']
            name=request.POST['name']
            email=request.POST['email']
            tel=request.POST['tel']
            agency=request.POST['agency']

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            user = User.objects.create(
                id=id,
                password=hashed_password.decode('utf-8'),
                name=name,
                email=email,
                tel=tel,
                agency=agency
            )
            user.save()
            
            return HttpResponseRedirect('')

    return render(request, 'map/signup.html')

def index(request):
    return render(request, 'map/index.html')


def main_new(request):

    return render(request, 'map/main_new.html')


# def sub_map(request):
#     return render(request, 'map/main_new/sub_map.html')

def sub_cctv(request):
    return render(request, 'map/main_new/sub_cctv.html')

def sub_record(request):
    return render(request, 'map/main_new/sub_record.html')

def sub_setting(request):
    return render(request, 'map/main_new/sub_setting.html')

def sub_stats(request):
    return render(request, 'map/main_new/sub_stats.html')


def sub_planning(request):
    return render(request, 'map/main_new/sub_planning.html')


def IdPopup(request):
    return render(request, 'map/main_new/IdPopup.html')

def PwPopup(request):
    return render(request, 'map/main_new/PwPopup.html')

def logout(request):
    auth.logout(request)
    return render(request, 'map/main_new/index.html')