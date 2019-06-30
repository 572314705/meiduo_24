from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SKU, GoodsCategory
from meiduo_admin.serializer.skus import SKUSerializer, GoodsCategorySerializer
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

    # 获取sku的所有三级分类信息
    @action(methods=['get'], detail=False)
    def categories(self, request):
        # 查询分类表获取三级分类
        goods = GoodsCategory.objects.filter(subs=None)
        # 返回所有的三级分类
        ser = GoodsCategorySerializer(goods, many=True)

        return Response(ser.data)
