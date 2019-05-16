from django.conf.urls import url

from users import views

urlpatterns = [
    url('index/', views.index,name='index')
]