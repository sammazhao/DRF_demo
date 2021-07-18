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

class Book(View):
    def get(self, request):
        # 1. 查询出数据对象
        book = BookInfo.objects.get(id=1)

        # 2. 借助序列化器类， 将需要返回的数据放到类里，得到对象，用.data取数据结果，直接返回
        ser = BookSerializer(book)
        return JsonResponse(ser.data)
