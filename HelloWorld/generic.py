class GenericAPIView():
    queryset=None
    serializer_class=None

    def get_queryset(self):
        """
        获取所有查询集数据
        :return:
        """
        return self.queryset


    # 提取正则匹配的pk值
    def get_object(self):

        """
        获取查询集中单一数据
        :return:
        """
        for instance in self.queryset:
            if instance.id==1:
                return instance

    def get_serializer(self,data=None):
        """
        获取指定序列化器对象
        :return:
        """
        serializer=self.serializer_class()
        return serializer(data=data)

    def get_serializer_class(self):
        """
        返回序列化器
        :return:
        """
        return self.serializer_class
