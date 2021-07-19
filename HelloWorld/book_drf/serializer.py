from rest_framework import serializers

# 嵌套的序列化器需要先定义出来，不然报错
# 指定对于英雄返回哪些字段, 英雄序列化器。 将他嵌套到BookSerializer序列化器中
# 形式3： 自定义嵌套序列化器
class HeroInfoSerializer(serializers.Serializer):
    # 一对多时：
    hname=serializers.CharField()
    hcomment=serializers.CharField()

    # 多对一时：
    # hbook=serializers.PrimaryKeyRelatedField()
    # hbook=serializers.StringRelatedField()


# 自定义序列化器
class BookSerializer(serializers.Serializer):
    # 定义需要返回的字段内容. 参考模型类中每个字段是什么类型，序列化器中就定义成什么类型
    # 序列化返回的字段
    btitle=serializers.CharField(max_length=20,min_length=5)
    bread=serializers.IntegerField(max_value=100,min_value=5)
    bpub_date=serializers.DateField() #这个字段必传
    bcomment=serializers.CharField(required=False)
    is_delete = serializers.CharField(default=False) #指定了默认值的话，即使是必填字段没传，会按照默认值传，不会报错
    # 其他的如allow_null


    #     指定所嵌套返回的其他信息, 字段中指定为外键
    # 形式1： 返回关联的英雄id
    # heroinfo_set=serializers.PrimaryKeyRelatedField(read_only=True,many=True)

    # 返回关联的英雄模型类的String方法值取到，返回给前端：
    # 形式2： 返回英雄name -- str 方法
    #     def __str__(self):
    #         return self.hname
    # heroinfo_set=serializers.StringRelatedField(read_only=True,many=True)
    # heroinfo_set  这种形式作为关联外键
    # heroinfo_set=HeroInfoSerializer(many=True)











