from django.conf.urls import url

from . import views

urlpatterns = [
    url('info/', views.info, name='info')
]