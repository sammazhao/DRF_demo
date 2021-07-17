"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# from django.conf.urls import url
# from . import views
# urlpatterns = [
#     url(r'^$', views.hello),
# ]

from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin
from . import views, testDB, search,search2, demoView
from books import views


urlpatterns = [
    # path('hello/', views.hello),
    # path('runoob2/', views.runoob2),
    # path('runoobList/', views.runoobList),
    # path('runoobD/', views.runoobD),
    # path('runoobDate/', views.runoobDate),
    # path('testdb/', testDB.testdb),
    # url(r'^admin/', admin.site.urls),
    path('runoob/', demoView.demoViewRender),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search2.search_post),
    url(r'^demoView/$', demoView.demoView),
    url(r'^TestModel/', include('TestModel.urls')),
    url(r'^', include('books.urls')),
    # url(r'^',views.BooksView)
]

