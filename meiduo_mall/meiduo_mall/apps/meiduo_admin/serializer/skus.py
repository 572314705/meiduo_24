from rest_framework import serializers

from goods.models import SKU, SKUSpecification, GoodsCategory, SpecificationOption, SPUSpecification


class SKUSpecificationSeriazier(serializers.ModelSerializer):
    """
           sku具体规格表序列化器
       """
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        # 指定根据那个模型类生成序列化器字段
        model = SKUSpecification
        # 指定那些字段生成
        fields = ('spec_id', 'option_id')


class SKUSerializer(serializers.ModelSerializer):
    """
            sku表序列化器

             "id": "商品SKU ID",
            "name": "商品SKU名称",
            "spu": "商品SPU名称",
            "spu_id": "商品SPU ID",
            "caption": "商品副标题",
            "category_id": "三级分类id",
            "category": "三级分类名称",
            "price": "价格",
            "cost_price": "进价",
            "market_price": "市场价格",
            "stock": "库存",
            "sales": "销量",
            "is_launched": "上下架",
            "specs": [
                {
                    "spec_id": "规格id",
                    "option_id": "选项id"
                },
                ...
            ]
        """
    # 关联嵌套序列化返回
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField(read_only=True)
    caption = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField(read_only=True)

    # 返回关联的sku具体规格表数据
    specs = SKUSpecificationSeriazier(many=True)

    class Meta:
        model = SKU
        fields = '__all__'


class GoodsCategorySerializer(serializers.ModelSerializer):
    """
            商品分类序列化器
        """

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class OptionSerialzier(serializers.ModelSerializer):
    """
           规格选项序列化器
       """

    class Meta:
        # 指定根据那个模型类生成序列化器字段
        model = SpecificationOption
        # 指定那些字段生成
        fields = ('id', 'value')

class SPUSpecificationSerialzier(serializers.ModelSerializer):
    """
            SPU规格表
             "id": "规格id",
            "name": "规格名称",
            "spu": "SPU商品名称",
            "spu_id": "SPU商品id",
            "options": [
                    {
                        "id": "选项id",
                        "name": "选项名称"
                    },
                    ...
        """
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    # 关联的规格选项表
    options = OptionSerialzier(many=True)
    class Meta:

        # 指定根据那个模型类生成序列化器字段
        model = SPUSpecification
        # 指定那些字段生成
        fields = "__all__"
