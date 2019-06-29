from django.conf import settings
from rest_framework import serializers

from goods.models import SKUImage, SKU
from fdfs_client.client import Fdfs_client


class ImageSerializer(serializers.ModelSerializer):
    # 关联嵌套查询
    sku = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SKUImage
        fields = ('id', 'image', 'sku')

    def create(self, validated_data):
        # self.context是个字典数据,里面保存了请求对象request
        sku_id=self.context['request'].data.get('sku')
        # 获取要保存的图片数据
        image_data = validated_data.get('image')
        # 链接FastDFS
        client = Fdfs_client(settings.FASTDFS_CONF)
        # 上传图片
        res = client.upload_by_buffer(image_data.read())
        # 判断上传状态
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError('上传图片失败')
        # 上传成功获取图片路径信息
        img_url = res['Remote file_id']
        # 将路径信息保存在图片表中
        image = SKUImage.objects.create(image=img_url, sku_id=sku_id)
        # 返回图片表对象
        return image



class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ('id', 'name')
