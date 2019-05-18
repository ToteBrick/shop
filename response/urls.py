from django.conf.urls import url

from . import views

urlpatterns = [
    url('res/', views.res)
]