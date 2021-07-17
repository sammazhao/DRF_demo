
# View 负责业务逻辑，并在适当时候调用 Model和 Template。

from django.http import  HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world!")

# def runoob(request):
#     context          = {}
#     context['hello']='Hello World'
#     return render(request, 'runoob.html', context)


# 增加一个新的对象，用于向模板提交数据  
def runoob(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)

from django.shortcuts import render

def runoob2(request):
  views_name = "菜鸟教程"
  return  render(request,"runoob.html", {"name":views_name})

def runoobList(request):
    views_list = ["菜鸟教程1","菜鸟教程2","菜鸟教程3"]
    return render(request, "runoobList.html", {"views_list": views_list})

def runoobD(request):
    views_dict = {"name":"菜鸟教程"}
    return render(request, "runoobD.html", {"views_dict": views_dict})

def runoobDate(request):
    import datetime
    now  =datetime.datetime.now()
    return render(request, "runoobDate.html", {"time": now})


