"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from django.urls import path  # django2.0

urlpatterns = [
    url('admin/', admin.site.urls),
    url('users/', include('users.urls',namespace='users')),
    url('goods/', include('goods.urls',namespace='goods')),
    url('request/', include('request.urls',namespace='request')),
    url('response/', include('response.urls',namespace='response')),
    url('classview/', include('classsview.urls')),
    url('mixin/', include('mixin.urls')),
    url('render/', include('render.urls')),
    url('book/', include('book.urls')),
    url(r'^', include('book.urls')), # 新增restful风格
    ]
    # path('admin/', admin.site.urls), django 2.0

