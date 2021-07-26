import json

from django.http import JsonResponse
from django.shortcuts import render
from book_drf.serializer import BookSerializer
from books.models import BookInfo
# 使用api view
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response


class Books(GenericAPIView):
    # 使用genericAPIView， 首先需要指定当前类视图中使用的查询集数据是什么
    queryset = BookInfo.objects.all()

    # 指定当前类视图使用的序列化器
    serializer_class = BookSerializer

    def get(self,request):
        # 1. 查询出数据对象. 获取查询集中的所有数据
        books=self.get_queryset()

        # 2. 使用指定序列化器获取序列化器对象
        ser=self.get_serializer(books,many=True)
        return Response(ser.data)

    # 保存方法
    def post(self,request):
#         1. 获取前端数据.
        data=request.data
#         2. 验证数据
        ser=self.get_serializer(data,many=True)
        ser.is_valid()
        # 3. 保存数据
        ser.save()
        return Response(ser.data)


class Book(GenericAPIView):
    def get(self, request):
        # 1. 查询出数据对象
        book = BookInfo.objects.get(id=1)

        # 2. 借助序列化器类， 将需要返回的数据放到类里，得到对象，用.data取数据结果，直接返回
        ser = BookSerializer(book)
        return JsonResponse(ser.data)

#更新方法, 针对单一数据的处理
class BookDRFView(GenericAPIView):
    # 使用genericAPIView， 首先需要指定当前类视图中使用的查询集数据是什么
    queryset = BookInfo.objects.all()
    # 指定当前类视图使用的序列化器
    serializer_class = BookSerializer

    def put(self, request, pk):
        # 1. 获取前端数据
        data=request.data
        # 先去查询出要更新的数据对象
        try:
            # 从查询集中获取指定的单一数据对象。 获取单一数据对象时，需要根据传过来的pk值，从查询集中找到id=pk的对象，然后把这个对象结果进行返回
            book = self.get_object()
        except:
            return Response({'error': 'errorMessage'}, status=400)
        # 使用序列化器改写：更新操作时，在进行序列化器初始化时，需要传一个需要更新的对象
        ser=BookSerializer(book,data=data)
        ser.is_valid()
        # 3. 更新数据
        ser.save()
        # 4. 返回结果, 进行序列化
        return Response(ser.data)

    def delete(self, request, pk):
        # 1. 查询数据对象
        # 注意！ get方法查询的数据不存在时，需要报错，这个点需要考虑！！
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return Response({'error': 'errorMessage'}, status=400)

        # 2. 进行删除操作
        # book.delete() 这个删除是物理删除，一般都是逻辑删除，所以不用这个方法
        book.is_delete=True
        book.save()
        return Response({})
