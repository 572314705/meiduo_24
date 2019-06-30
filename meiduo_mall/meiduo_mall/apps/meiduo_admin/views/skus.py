from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import SKU
from meiduo_admin.serializer.skus import SKUSerializer
from meiduo_admin.utils import PageNum


class SKUViewSet(ModelViewSet):
    # 指定序列化器
    serializer_class = SKUSerializer
    # 指定查询集
    queryset = SKU.objects.all()
    # 指定分页器
    pagination_class = PageNum
    # 指定权限
    permission_classes = [IsAdminUser]
