from rest_framework import serializers

# 自定义序列化器
class BookSerializer(serializers.Serializer):
    # 定义需要返回的字段内容. 参考模型类中每个字段是什么类型，序列化器中就定义成什么类型
    # 序列化返回的字段
    btitle=serializers.CharField()
    bread=serializers.IntegerField()
    bpub_date=serializers.DateField()




