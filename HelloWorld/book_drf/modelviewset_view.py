from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from books.models import BookInfo
from serializer import BookSerializer


class Books(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookSerializer

    # 指定不同的方法，在调用的时候用哪个序列化器
    def get_serializer_class(self):
        if self.action=='lastdata':
            return BookSerializer
        else:
            return BookSerializer

    #True: 生成一个带pk匹配的路由规则
    @action(methods=['get'],detail=True)
    def lastdata(self,request,pk):
        #提取的是当前请求的方法的方法名。 作用： 判断当前请求的方法是谁？根据不同的请求，返回不同的序列化器
        print(self.action)
        book=BookInfo.objects.get(id=pk)
        ser=self.get_serializer(book)
        return Response(ser.data)