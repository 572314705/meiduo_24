from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.serializer.images import ImageSerializer, SKUSerializer
from meiduo_admin.utils import PageNum


class ImageView(ModelViewSet):
    # 指定序列化器
    serializer_class = ImageSerializer
    # 指定查询集
    queryset = SKUImage.objects.all()
    # 指定分页器
    pagination_class = PageNum
    # 指定权限
    permission_classes = [IsAdminUser]

    # 在保存图片之前先获取SKU数据
    def simple(self, requst):
        # 获取SKU数据
        skus = SKU.objects.all()

        # 序列化返回
        ser = SKUSerializer(skus, many=True)
        return Response(ser.data)
