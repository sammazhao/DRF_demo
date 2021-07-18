from django.db import models

# Create your models here.
# 定义图书模型类 booksInfo -- 相当于一张table
class BookInfo(models.Model):
    objects = None
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread  =models.IntegerField(default=0,verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    # 类中定义meta类，meta类是对象属性，相当于BookInfo的一个属性
    # 作用：来控制BookInfo类本身进行哪些操作。 针对于整张表进行控制的时候，这个属性定义在Meta类中
    # 如果只是对表的某个字段进行定义的话，在外面定义
    class Meta:
        db_table = 'tb_books' # 知名数据库表名
        verbose_name = '图书' # 在admin站点中显示的名称
        verbose_name_plural = verbose_name # 显示的复数名称


    def __str__(self):
        '''定义每个数据对象的显示信息'''
        return self.btitle

# # 定义英雄模型类HeroInfo
# class HeroInfo(models.Model):
#     GENDER_CHOICE = (
#         (0, 'male'),
#         (1, 'female')
#     )
#     hname = models.CharField(max_length=20,verbose_name='名称')
#     hgender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0, verbose_name='性别')
#     hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
#     hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
#     is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')
#
#     class Meta:
#         db_table = 'tb_heros'
#         verbose_name = '英雄'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.hname