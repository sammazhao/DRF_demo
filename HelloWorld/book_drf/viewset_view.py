import json

from django.http import JsonResponse
from book_drf.serializer import BookSerializer
from books.models import BookInfo
# 使用api view
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response



class Books(ViewSet):
    def list(self, request):
        # 1. 查询出数据对象， 查询字符串数据用query_params,作用和GET一样
        print(request.query_params)
        books = BookInfo.objects.all()

        #  在视图类中，调用序列化器类
        # 2. 借助序列化器类， 将需要返回的数据放到类里，得到对象，用.data取数据结果，直接返回
        # 返回多个数据对象时候，many=True，才能返回多个数据
        ser = BookSerializer(books, many=True)
        return Response(ser.data)

    # 保存方法
    def create(self, request):
        #         1. 获取前端数据.data属性获取请求体里的数据并且直接转化成字典类型，不需要再转化
        data = request.data
        #         2. 验证数据
        ser = BookSerializer(data=data)
        # ser.is_valid(raise_exception=True) #验证方法。 调用这个方法后，会进入序列化器中验证字段指定的选项参数.# raise_exception=True, 出错后自动返回error信息
        ser.is_valid()
        # 3. 保存数据,调用序列化器中的create()
        ser.save()
        print(ser.validated_data)
        return Response(ser.data)

#更新方法, 针对单一数据的处理
class BookDRFView(ViewSet):
    # 使用genericAPIView， 首先需要指定当前类视图中使用的查询集数据是什么
    def update(self, request, pk):
        # 1. 获取前端数据。通过.body方式，因为前端传送数据是在请求body中
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

    def lastdata(self,request,pk):
        book = BookInfo.objects.get(id=pk)
        ser=BookSerializer(book)
        return Response(ser.data)




class Book(ViewSet):
    def get(self, request):
        # 1. 查询出数据对象
        book = BookInfo.objects.get(id=1)

        # 2. 借助序列化器类， 将需要返回的数据放到类里，得到对象，用.data取数据结果，直接返回
        ser = BookSerializer(book)
        return JsonResponse(ser.data)

