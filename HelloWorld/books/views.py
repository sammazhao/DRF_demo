from django.shortcuts import render
from django.views import View
from books import models
from books.models import BookInfo
from django.http import JsonResponse
# Create your views here.

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
                    'id':book.id,
                    'btitle':book.btitle,
                    'bread': book.bread,
                    'bcomment': book.bcomment,
                    'bpub_date': book.bpub_date,
                }
            )

        return JsonResponse(books_list,safe=False)
        # 在Django中，使用JSON传输数据，有两种方式，一种是使用Python的JSON包，一种是使用Django的JsonResponse
        # 列表数据操作的时候，需要加这个，才能转换成数组的形式返回



    def post(self, request):
        pass
        # 1. 获取前端数据
        # 2. 验证数据
        # 3. 保存数据
        # 4. 返回结果



class BookView(View):
    '''获取单一数据，更新，删除'''
    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
