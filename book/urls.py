from django.conf.urls import url

from . import views

urlpatterns = [
    url('info/', views.info, name='info'),  # 增
    url('delete/', views.delete),  # 删
    url('update/', views.update),  # 修改
    url('query/', views.query),    # 查
]