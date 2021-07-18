from django.conf.urls import url
from django.contrib import  admin
from . import views
urlpatterns = [
    # url(r'^books/$', views.Boo.as_view()),
    #
    # # 对于单一资源数据，匹配他的id值
    # url(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
    url(r'^books_drf/$', views.Books.as_view()),
    url(r'^book_drf/$', views.Book.as_view())
]