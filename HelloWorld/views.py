from generic import GenericAPIView
from serializer import BookSerializer

class BookView(GenericAPIView):

    queryset = [{'btitle':'111','id':'1'}]
    serializer_class = BookSerializer
    def post(self,request):
        #1. 获取数据
        data=request.data

        # 2. 验证数据
        ser=self.get_serializer(data=data)
        ser.is_valid()

        # 3. 保存数据
        ser.save()

        # 4. 返回结果
        return ser.data


