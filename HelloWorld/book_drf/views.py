import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from book_drf.serializer import BookSerializer
from books.models import BookInfo


class Books(View):
    def get(self,request):
        # 1. 查询出数据对象
        books=BookInfo.objects.all()

        #  在视图类中，调用序列化器类
        # 2. 借助序列化器类， 将需要返回的数据放到类里，得到对象，用.data取数据结果，直接返回
        # 返回多个数据对象时候，many=True，才能返回多个数据
        ser=BookSerializer(books,many=True)
        return JsonResponse(ser.data,safe=False)

    def post(self,request):
#         1. 获取前端数据
        data=request.body.decode()
        data_dict=json.loads(data)
#         2. 验证数据
        ser=BookSerializer(data=data_dict)
        ser.is_valid(raise_exception=True) #验证方法。 调用这个方法后，会进入序列化器中验证字段指定的选项参数.
                                            # raise_exception=True, 出错后自动返回error信息
        return JsonResponse(ser.errors)


class Book(View):
    def get(self, request):
        # 1. 查询出数据对象
        book = BookInfo.objects.get(id=1)

        # 2. 借助序列化器类， 将需要返回的数据放到类里，得到对象，用.data取数据结果，直接返回
        ser = BookSerializer(book)
        return JsonResponse(ser.data)
