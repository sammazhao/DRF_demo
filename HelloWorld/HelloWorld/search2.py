# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf


# ===================== 以下为POST方法，用一个URL和处理函数，同时显示视图和处理请求 ======================
# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)