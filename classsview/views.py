from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


def decorator(fn):
    def wrapper(self, request, *args, **kwargs):
        print(request.method, request.path)
        return fn(self, request, *args, **kwargs)

    return wrapper


class LoginView(View):

    @decorator
    def get(self, request):
        return HttpResponse('get 请求')

    @decorator
    def post(self, request):
        return HttpResponse('post 请求')
