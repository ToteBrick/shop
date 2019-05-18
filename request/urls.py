from django.conf.urls import url

from . import views

urlpatterns = [
    url('login_connect/([a-z]+)/(\d+)', views.login_connect, name='login'), # 正则匹配,
   # 命名参数按名字传递
    url('login_connect2/(?P<city>[a-z]+)/(?P<code>\d+)', views.login_connect_sort, name='login'),
   # 字符串拼接参数
    url('query',views.query)
]
