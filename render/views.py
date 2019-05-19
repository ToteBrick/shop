from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'city': '成都'}
    return render(request, 'index.html', context)