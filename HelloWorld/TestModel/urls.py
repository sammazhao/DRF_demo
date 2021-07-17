from django.contrib import admin
from django.conf.urls import url
# from django.urls import path
# from . import views
from TestModel import views
urlpatterns = [
    url('add_book/', views.add_book),
    url('queryAll/', views.queryAll),
    url('queryByFilter/', views.queryByFilter),
    url('delete/', views.delete),
]