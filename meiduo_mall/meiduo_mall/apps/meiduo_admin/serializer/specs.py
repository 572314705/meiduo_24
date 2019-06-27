from rest_framework import serializers

from goods.models import SPUSpecification


class SpecsSerializer(serializers.ModelSerializer):
    # 关联嵌套序列化返回
    # 指定ｓｐｕ名称
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()

    class Meta:
        # 指定是根据那个模型类生成的序列化器
        model = SPUSpecification
        # 生成的字段
        fields = ('id', 'name', 'spu', 'spu_id')


class SPUSerializer(serializers.ModelSerializer):


    class Meta:
        # 指定是根据那个模型类生成的序列化器
        model = SPUSpecification
        # 生成的字段
        fields = ('id', 'name')
