from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def res(request):
    response = HttpResponse(content='response body',status=200,content_type='text/html')
    # json格式的格式为content_type='application/json'
    return response