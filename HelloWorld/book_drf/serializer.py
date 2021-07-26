from rest_framework import serializers
from books.models import BookInfo
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

# 对某个单一字段执行验证方法
def bread_valid():
    print("验证逻辑")

# 自定义序列化器
class BookSerializer(serializers.Serializer):
    # 定义需要返回的字段内容. 参考模型类中每个字段是什么类型，序列化器中就定义成什么类型
    # 序列化返回的字段
    btitle=serializers.CharField(max_length=20,min_length=5)
    bread=serializers.IntegerField(max_value=100,min_value=5,validators=bread_valid())
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


    # 自定义验证方法
     #单一字段验证
    def validate_btitle(self, value):
        if value =='python':
            raise serializers.ValidationError('书名不能是python')
        return value


    # # 多个字段验证
    # def validate(self,attrs):
    #     if attrs['bread'] > attrs['bcomment']:
    #         raise serializers.ValidationError('阅读量大于了评论量')
    #     return attrs

    # 保存数据的步骤封装到序列化器的create方法中， 然后在views中调用
    def create(self, validated_data):
        # 保存数据, 参数validated_data 是字典
        # 方式一：
        # BookInfo.objects.create(btitle=validated_data['btitle'])

        # 方式二， 对字典进行拆包处理，e.g: {'name':'python'}, 处理后  name=python
        book=BookInfo.objects.create(**validated_data)
        return book


    # 更新数据的步骤封装到update方法中，然后在views中调用
    # instance: 在序列化器初始化时，传递过来的数据对象
    def update(self,instance,validated_data):
        instance.btitle=validated_data['btitle']
        instance.save()
        return instance


# 模型类序列化器
class BookModelSerializer(serializers.ModelSerializer):

    # 修改，增加字段选项
    #方式一，显式指明,也可以新增字段（模型类里没有 的字段，要在fields里包含这个字段）
    bread=serializers.IntegerField(max_value=100,min_value=20)
    class Meta:
        model=BookInfo   # 指定生成字段的模型类
        #接下来指定哪些字段，作为序列化器字段。指定模型类中的字段
        fields=('btitle','bread')
        read_only=('btitle',)
        # fields='__all__'  # 指定所有字段
        exlcude=('bcomment',)  #取反操作， 除了这个字段之外的都生成

        # 方式二，通过extra字段更改， 增加
        extra_kwargs={
            "bcomment":{
                "max_value":100
            },
            "btitle": {
                "min_value": 10
            }
        }

















