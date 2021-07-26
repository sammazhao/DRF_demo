import json

from django.http import JsonResponse
from django.shortcuts import render
from book_drf.serializer import BookSerializer
from books.models import BookInfo
# 使用api view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.response import Response


class Books(GenericAPIView,CreateModelMixin,ListModelMixin):
    # 使用genericAPIView， 首先需要指定当前类视图中使用的查询集数据是什么
    queryset = BookInfo.objects.all()

    # 指定当前类视图使用的序列化器
    serializer_class = BookSerializer

    # 使用拓展类后，所有业务逻辑的代码都交给拓展类中封装的方法来实现
    def get(self,request):
        return self.list(request)

    # 保存方法
    def post(self,request):
        return self.create(request)



class Book(GenericAPIView):
    def get(self, request):
        # 1. 查询出数据对象
        book = BookInfo.objects.get(id=1)

        # 2. 借助序列化器类， 将需要返回的数据放到类里，得到对象，用.data取数据结果，直接返回
        ser = BookSerializer(book)
        return JsonResponse(ser.data)

#更新方法, 针对单一数据的处理
class BookDRFView(GenericAPIView,UpdateModelMixin,DestroyModelMixin):
    # 使用genericAPIView， 首先需要指定当前类视图中使用的查询集数据是什么
    queryset = BookInfo.objects.all()
    # 指定当前类视图使用的序列化器
    serializer_class = BookSerializer

    def put(self, request, pk):
        return self.update(request,pk)

    def delete(self, request, pk):
        return self.destroy(request,pk)
