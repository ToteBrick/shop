from django.conf.urls import url

from . import views

urlpatterns = [
    url('index/', views.index),
    url('filter/', views.filter),
    url('jiaja/', views.jiaja),
]