from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse
from TestModel import models
def add_book(request):
    books = models.Book.objects.create(title="书名",price=200,publish="喵喵版社3",pub_date="2010-10-10")
    print(books, type(books)) # Book object (18)
    return HttpResponse("<p>数据添加成功！</p>")


# 使用 all() 方法来查询所有内容。
def queryAll(request):
    books = models.Book.objects.all()
    print(books, type(books))
    return HttpResponse("<p>数据查询成功！</p>")

# filter() 方法用于查询符合条件的数据。
def queryByFilter(request):
    books = models.Book.objects.filter(pk=3)
    print(books)
    print('////////////////////////////////')
    books = models.Book.objects.filter(publish='喵喵版社', price=200)
    # 查询所有的id字段和price字段的数据
    books = models.Book.objects.values("pk","price")
    print('***********************************************')
    print(books)
    print(books[0]["price"],type(books)) # 得到的是第一条记录的price字段的数据
    print(books)
    return HttpResponse("<p>查找成功！</p>")

def delete(request):
    books=models.Book.objects.filter(pk__in=[1,2]).delete()
    print(books, type(books))
    return HttpResponse("<p>数据删除成功！</p>")


# 返回的是 QuerySet 类型数据，类似于 list，里面不是模型类的对象，而是一个可迭代的字典序列，字典里的键是字段，值是数据。

