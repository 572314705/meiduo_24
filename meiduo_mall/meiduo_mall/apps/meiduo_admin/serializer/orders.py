from rest_framework import serializers

from goods.models import SKU
from orders.models import OrderInfo, OrderGoods

class SKUSerializer(serializers.ModelSerializer):
    '''SKU'''
    class Meta:
        model = SKU
        fields = ('name','default_image')

class OrderGoodsSerialzier(serializers.ModelSerializer):
    """
            订单商品表
        """
    sku = SKUSerializer()
    class Meta:
        model = OrderGoods
        fields = ('count','price','sku')

class OrderSerializer(serializers.ModelSerializer):
    """
            订单表序列化
        """
    user = serializers.StringRelatedField(read_only=True)
    address = serializers.StringRelatedField(read_only=True)

    skus = OrderGoodsSerialzier(many=True)
    class Meta:
        # 指定根据那个模型类生成序列化器字段
        model = OrderInfo
        # 指定那些字段生成
        fields = '__all__'