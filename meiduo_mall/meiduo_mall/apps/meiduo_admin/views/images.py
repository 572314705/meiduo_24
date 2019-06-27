from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage
from meiduo_admin.serializer.images import ImageSerializer
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
