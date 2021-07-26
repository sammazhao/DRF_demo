from django.conf.urls import url
from django.contrib import admin
from . import views,apiview_view,genericapiview_view,mixin_view,childmixin_view,viewset_view,genericviewset_view,modelviewset_view
from rest_framework.routers import SimpleRouter,DefaultRouter
urlpatterns = [
    # url(r'^books/$', views.Boo.as_view()),
    #
    # # 对于单一资源数据，匹配他的id值
    # # url(r'^books/(?P<pk>\d+)/$', views.BookView.as_view()),
    # url(r'^books_drf/$', views.Books.as_view()),
    # url(r'^book_drf/$', views.Book.as_view()),
    # url(r'^books_drf/(?P<pk>\d+)/$', views.BookDRFView.as_view())

    # url(r'^books_drf/$', apiview_view.Books.as_view()),  #获取所有图书
    # url(r'^book_drf/$', apiview_view.Book.as_view()),   #保存图书
    # url(r'^books_drf/(?P<pk>\d+)/$', apiview_view.BookDRFView.as_view()),  #匹配单个书进行增删改
    #
    # url(r'^books_drf/$', genericapiview_view.Books.as_view()),  # 获取所有图书
    # url(r'^book_drf/$', genericapiview_view.Book.as_view()),  # 保存图书
    # url(r'^books_drf/(?P<pk>\d+)/$', genericapiview_view.BookDRFView.as_view())  # 匹配单个书进行增删改
    # url(r'^books_drf/$', mixin_view.Books.as_view()),  # 获取所有图书
    # url(r'^book_drf/$', mixin_view.Book.as_view()),  # 保存图书
    # url(r'^books_drf/(?P<pk>\d+)/$', mixin_view.BookDRFView.as_view())  # 匹配单个书进行增删改
    # url(r'^books_drf/$', childmixin_view.Books.as_view()),  # 获取所有图书
    # url(r'^book_drf/$', childmixin_view.Book.as_view()),  # 保存图书
    # url(r'^books_drf/(?P<pk>\d+)/$', childmixin_view.BookDRFView.as_view())  # 匹配单个书进行增删改

    # # ViewSet路由使用, 当匹配的方法名是默认的5个时
    # url(r'^books_drf/$', viewset_view.Books.as_view({'get':'list','post':'create'})),  # 获取所有图书
    # # url(r'^book_drf/$', viewset_view.Book.as_view()),  # 保存图书
    # url(r'^books_drf/(?P<pk>\d+)/$', viewset_view.BookDRFView.as_view({'put':'update'})), # 匹配单个书进行增删改
    #
    # # ViewSet路由使用, 当匹配的方法名是其他的时
    # url(r'^books_drf/(?P<pk>\d+)/lastdata/$', viewset_view.BookDRFView.as_view({'get':'lastdata'}))  # 匹配单个书进行增删改

    # generic ViewSet路由使用, 当匹配的方法名是默认的5个时
    # url(r'^books_drf/$', genericviewset_view.Books.as_view({'get': 'list', 'post': 'create'})),  # 获取所有图书
    # url(r'^books_drf/(?P<pk>\d+)/$', genericviewset_view.BookDRFView.as_view({'put': 'update'})),  # 匹配单个书进行增删改
    # url(r'^books_drf/(?P<pk>\d+)/lastdata/$', genericviewset_view.BookDRFView.as_view({'get': 'lastdata'}))  # 匹配单个书进行增删改

    # url(r'^books_drf/$', modelviewset_view.Books.as_view({'get': 'list', 'post': 'create'})),  # 获取所有图书
    # url(r'^books_drf/(?P<pk>\d+)/$', modelviewset_view.Books.as_view({'put': 'update','get':'retrieve','delete':'destroy'})),  # 匹配单个书进行增删改
]

# 自动生成路由。必须和视图集匹配使用
# router=SimpleRouter()
router=DefaultRouter()
#路由生成方法。 参数：路径，调用哪个模型类，命名路由
router.register('books_drf',modelviewset_view.Books,base_name='books')
print(router.urls)
urlpatterns+=router.urls
