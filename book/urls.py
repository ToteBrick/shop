from django.conf.urls import url

from . import views
from . import views_xu


urlpatterns = [
    url('info/', views.info, name='info'),  # 增
    url('delete/', views.delete),  # 删
    url('update/', views.update),  # 修改
    url('query/', views.query),  # 查
    # url(r'^books/$', views.BooksView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
    url(r'^books/$', views_xu.BooksView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', views_xu.BookView.as_view()),
]
