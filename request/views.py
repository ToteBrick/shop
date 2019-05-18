from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_connect(request,city,code):

    # param = request.GET
    print('city:',city)
    print('code:',code)
    return HttpResponse('URL路径拼接')