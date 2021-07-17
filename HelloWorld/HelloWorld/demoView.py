from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# def demoView(request):
#     name = request.GET.get("name")
#     return HttpResponse('姓名：{}'.format(name))
from django.shortcuts import render

@csrf_exempt
def demoView(request):
    name = request.POST.get("name")
    return HttpResponse('姓名：{}'.format(name))

    # return HttpResponse("<a href='https://www.baidu.com/'>百度一下</a>")

@csrf_exempt
def demoViewRender(request):
    name = "xxxxxx"
    # return HttpResponse('姓名：{}'.format(name))
    # render(): 返回文本，第一个参数为 request，第二个参数为字符串（页面名称），
    # 第三个参数为字典（可选参数，向页面传递的参数：键为页面参数名，值为views参数名）。
    return render(request,"runoob.html",{"name":name})