from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# 1. 提取正则url特定参数
def login_connect(request, city, code):
    # param = request.GET
    print('city:', city)
    print('code:', code)
    return HttpResponse('URL路径拼接')


# 参数无序，按正则名称匹配
def login_connect_sort(request, code, city):
    # param = request.GET
    print('city:', city)
    print('code:', code)
    return HttpResponse('URL路径拼接按名称匹配')
