from django.conf.urls import url
from django.contrib import  admin
from . import views
urlpatterns = [
    url(r'^books/$', views.BooksView.as_view()),

    # 对于单一资源数据，匹配他的id值
    url(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
    # url(r'^books_drf/(?P<pk>\d+)/$', views.BooksView.as_view()),
]