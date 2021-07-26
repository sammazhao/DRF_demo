import json

from django.http import JsonResponse
from django.shortcuts import render
from book_drf.serializer import BookSerializer
from books.models import BookInfo
# 使用api view
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class Books(APIView):
    def get(self,request):
        # 1. 查询出数据对象， 查询字符串数据用query_params,作用和GET一样
        print(request.query_params)
        books=BookInfo.objects.all()

        #  在视图类中，调用序列化器类
        # 2. 借助序列化器类， 将需要返回的数据放到类里，得到对象，用.data取数据结果，直接返回
        # 返回多个数据对象时候，many=True，才能返回多个数据
        ser=BookSerializer(books,many=True)
        return Response(ser.data)

    # 保存方法
    def post(self,request):
#         1. 获取前端数据.data属性获取请求体里的数据并且直接转化成字典类型，不需要再转化
        data=request.data
#         2. 验证数据
        ser=BookSerializer(data=data)
        # ser.is_valid(raise_exception=True) #验证方法。 调用这个方法后，会进入序列化器中验证字段指定的选项参数.# raise_exception=True, 出错后自动返回error信息
        ser.is_valid()
        # 3. 保存数据,调用序列化器中的create()
        ser.save()
        print(ser.validated_data)
        return Response(ser.data)


class Book(APIView):
    def get(self, request):
        # 1. 查询出数据对象
        book = BookInfo.objects.get(id=1)

        # 2. 借助序列化器类， 将需要返回的数据放到类里，得到对象，用.data取数据结果，直接返回
        ser = BookSerializer(book)
        return JsonResponse(ser.data)

#更新方法
class BookDRFView(APIView):

    def put(self, request, pk):
        # 1. 获取前端数据。通过.body方式，因为前端传送数据是在请求body中
        # request.body是bite类型的数据，需要decode, 得到string形式的json，即加了""的字典
        # data = request.body.decode()
        # 转成dict
        # data_dict = json.loads(data)

        data=request.data
        # 先去查询出要更新的数据对象
        try:
            book = BookInfo.objects.get(id=pk)
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
