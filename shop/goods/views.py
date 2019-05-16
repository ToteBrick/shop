from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def login(request):
    url = reverse('goods:login') # 域名反向解析
    return redirect('users:index') # 重定向
    # return HttpResponse(url)