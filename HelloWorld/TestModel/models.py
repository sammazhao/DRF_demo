from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    objects = None
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入

    title = models.CharField(max_length=32) # 书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2) # 书籍价格
    publish = models.CharField(max_length=32) # 出版社名称

    # 加上read_only 表示这个字段不参与反序列化的验证和保存过程，只参与序列化返回
    pub_date = models.DateField() # 出版时间