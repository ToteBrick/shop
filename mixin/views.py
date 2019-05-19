from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from classsview.views import decorator_noself, decorator

'''
定义扩展类
'''



class DecoratorMixin(object):
    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        # view = decorator(view)
        view = decorator_noself(view)
        return view


# 调用扩展类
class DemoView(DecoratorMixin, View):
    def get(self, request):
        return HttpResponse('get方法')

    def post(self, request):
        return HttpResponse('post方法')
