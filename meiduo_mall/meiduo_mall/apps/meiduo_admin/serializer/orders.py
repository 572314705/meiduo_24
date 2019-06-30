from rest_framework import serializers

from orders.models import OrderInfo


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定根据那个模型类生成序列化器字段
        model = OrderInfo
        # 指定那些字段生成
        fields = ('order_id', 'create_time')