from rest_framework import serializers

from goods.models import SKUImage


class ImageSerializer(serializers.ModelSerializer):
    # 关联嵌套查询
    sku = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SKUImage
        fields = ('id', 'image', 'sku')
