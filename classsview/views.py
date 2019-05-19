from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class LoginView(View):

    def get(self,request):

        return HttpResponse('get 请求')
