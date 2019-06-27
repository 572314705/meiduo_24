from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import SPUSpecification
from meiduo_admin.serializer.specs import SpecsSerializer
from meiduo_admin.utils import PageNum


class SpecsView(ModelViewSet):

    # 指定序列化器
    serializer_class = SpecsSerializer
    # 指定查询集
    queryset = SPUSpecification.objects.all()
    # 指定分页器
    pagination_class = PageNum
    # 指定权限
    permission_classes = [IsAdminUser]
