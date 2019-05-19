from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View


def decorator(fn):
    def wrapper(self, request, *args, **kwargs):
        print(request.method, request.path)
        return fn(self, request, *args, **kwargs)

    return wrapper


def decorator_noself(fn):
    def wrapper(request, *args, **kwargs):
        print(request.method, request.path)
        return fn(request, *args, **kwargs)

    return wrapper


class LoginView(View):

    @decorator
    def get(self, request):
        return HttpResponse('get 请求')

    @decorator
    def post(self, request):
        return HttpResponse('post 请求')


'''
调用django封装的类装饰器语法糖
'''


@method_decorator(decorator_noself, name='dispatch')
class LoginViewDecorator(View):

    def get(self, request):
        return HttpResponse('get 请求')

    def post(self, request):
        return HttpResponse('post 请求')
