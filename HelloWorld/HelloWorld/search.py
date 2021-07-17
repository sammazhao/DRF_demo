from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect

from django import template


# ===================== 以下为GET方法，将视图显示和请求处理分成两个方法进行 ======================
# 表单, 用于接收用户请求
def search_form(request):
    return render(request, 'search_form.html')

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

