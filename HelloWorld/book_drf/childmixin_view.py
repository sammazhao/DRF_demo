import json

from django.http import JsonResponse
from book_drf.serializer import BookSerializer
from books.models import BookInfo
# 使用api view
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView



class Books(ListCreateAPIView):
    # 使用genericAPIView， 首先需要指定当前类视图中使用的查询集数据是什么
    queryset = BookInfo.objects.all()

    # 指定当前类视图使用的序列化器
    serializer_class = BookSerializer

#更新方法, 针对单一数据的处理
class BookDRFView(RetrieveUpdateDestroyAPIView):
    # 使用genericAPIView， 首先需要指定当前类视图中使用的查询集数据是什么
    queryset = BookInfo.objects.all()
    # 指定当前类视图使用的序列化器
    serializer_class = BookSerializer


class Book(GenericAPIView):
    def get(self, request):
        # 1. 查询出数据对象
        book = BookInfo.objects.get(id=1)

        # 2. 借助序列化器类， 将需要返回的数据放到类里，得到对象，用.data取数据结果，直接返回
        ser = BookSerializer(book)
        return JsonResponse(ser.data)

