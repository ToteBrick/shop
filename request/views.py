import json

from django.http import HttpResponse, JsonResponse
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


# 查询字符串
def query(request):
    param = request.GET
    # / request / query / ?name = 'Jim' & age = 18
    name = param.get('name')
    age = param.get('age')
    print(name, age)
    return HttpResponse('查询字符串')


# 表单数据 form_data
def form_data(request):
    password = request.POST.get('password')
    print(password)
    return HttpResponse('form_data')


# 非表单数据，典型的json
def json_parse_data(request):
    str_data = request.body.decode('utf-8')
    dict = json.loads(str_data)
    print(dict)  # 可用postman演示json请求 {'name': 'Tom', 'age': 18}
    return HttpResponse('json parse')


# 非表单数据，典型的json，方式二
def json_parse(request):
    dict = {'name': 'Tom', 'age': 18}
    list = [{'name': 'Tom', 'age': 18}, {'name': 'Alice', 'age': 20}]
    # return JsonResponse(dict)
    return JsonResponse(list, safe=False) # 传列表要设置safe为False
