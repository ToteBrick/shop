from django.conf.urls import url

from . import views

urlpatterns = [
    url('login/', views.LoginView.as_view()),
    url('login_decorator/', views.LoginViewDecorator.as_view()),
]