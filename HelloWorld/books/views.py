from django.shortcuts import render
from django.views import View
from books import models
from books.models import BookInfo
from django.http import JsonResponse
import json
from rest_framework.generics import ListCreateAPIView,\
    CreateAPIView,UpdateAPIView,RetrieveDestroyAPIView,DestroyAPIView


'''
在views中最核心的事情： 
- 将数据库的数据序列化为前端所需要的格式，并返回
- 将前端发送的数据烦了序列化为模型类的对象，并保存到db中
'''

class BooksView(View):
    '''获取所有图书和保存'''

    def get(self, request):
        # 1. 查询图书对象 [{},{},{}]
        books = BookInfo.objects.all()
        # 2. 返回图书数据. 返回时不能直接返回图书对象，因为图书对象代表的数据在server上保存的，
        # 如果现在返回前端，在浏览器上，用户不知道对象对应的数据是谁
        # 因此返回时要把对象中所对应的所有字段的数据，返回给前端
        # 思路：创建一个空列表，转换成数组的形式，返回给前端
        books_list = []
        for book in books:
            books_list.append(
                {
                    'id': book.id,
                    'btitle': book.btitle,
                    'bread': book.bread,
                    'bcomment': book.bcomment,
                    'bpub_date': book.bpub_date,
                }
            )

        return JsonResponse(books_list, safe=False)
        # 在Django中，使用JSON传输数据，有两种方式，一种是使用Python的JSON包，一种是使用Django的JsonResponse
        # 列表数据操作的时候，需要加这个，才能转换成数组的形式返回

    def post(self, request):
        # 1. 获取前端数据。通过.body方式，因为前端传送数据是在请求body中
        # request.body是bite类型的数据，需要decode, 得到string形式的json，即加了""的字典
        data = request.body.decode()
        # 转成dict
        # =========== 反序列化 =============
        data_dict = json.loads(data)

        # 2. 验证数据
        # 用.get方式更安全，如果前端没有返回这个字段，返回None
        btitle = data_dict.get('btitle')
        bpub_date = data_dict.get('bpub_date')

        # 验证的例子：非空校验。还有一些其他的验证，如max length等
        if bpub_date is None or btitle is None:
            return JsonResponse({'error': 'errorMessage'}, status=400)

        # 3. 保存数据
        book = BookInfo.objects.create(btitle=btitle, bpub_date=bpub_date)
        # =========== 反序列化结束 =============

        # 4. 返回结果, 进行序列化
        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'bpub_date': book.bpub_date,
            }
        )


class BookView(View):
    pass
    '''获取单一数据，更新，删除'''

    def get(self, request,pk):
        # 1. 查询数据对象
        # 注意！ get方法查询的数据不存在时，需要报错，这个点需要考虑！！
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'errorMessage'}, status=400)

        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'bpub_date': book.bpub_date,
            }
        )

    def put(self, request, pk):
        # 1. 获取前端数据。通过.body方式，因为前端传送数据是在请求body中
        # request.body是bite类型的数据，需要decode, 得到string形式的json，即加了""的字典
        data = request.body.decode()
        # 转成dict
        data_dict = json.loads(data)

        # 2. 验证数据
        # 用.get方式更安全，如果前端没有返回这个字段，返回None
        btitle = data_dict.get('btitle')
        bpub_date = data_dict.get('bpub_date')

        # 验证的例子：非空校验。还有一些其他的验证，如max length等
        if bpub_date is None or btitle is None:
            return JsonResponse({'error': 'errorMessage'}, status=400)

        # 3. 更新数据
        # 先去查询出要更新的数据对象
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'errorMessage'}, status=400)
        book.btitle=btitle
        book.bpub_date=bpub_date
        book.save()

        # 4. 返回结果, 进行序列化
        return JsonResponse(
            {
                'id': book.id,
                'btitle': book.btitle,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'bpub_date': book.bpub_date,
            }
        )

    def delete(self, request, pk):
        # 1. 查询数据对象
        # 注意！ get方法查询的数据不存在时，需要报错，这个点需要考虑！！
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': 'errorMessage'}, status=400)

        # 2. 进行删除操作
        # book.delete() 这个删除是物理删除，一般都是逻辑删除，所以不用这个方法
        book.is_delete=True
        book.save()
        return JsonResponse({})

