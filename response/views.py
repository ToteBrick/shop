from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def res(request):
    response = HttpResponse(content='response body',status=200,content_type='text/html')
    # json格式的格式为content_type='application/json'
    return response

# 设置Cookie与读取Cookie
def cook_test(request):

    response = HttpResponse('cookie')
    response.set_cookie('name','Alice') # 设置cookie
    print(request.COOKIES.get('name'))  # 读取指定Cookie
    return response


def session_test(request):
    session = HttpResponse('session')
    request.session['weather'] = 'sunny'  # 设置指定session ,会在cookie里设置sessionid
    weather = request.session['weather']  # 读取session
    print(weather)
    return session