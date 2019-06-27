from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from goods.models import SPUSpecification, SPU
from meiduo_admin.serializer.specs import SpecsSerializer, SPUSerializer
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

    # @action(methods=['get'], detail=False)
    def simple(self,request):
        # 查询所有Ｓｐｕ信息
        spus = SPU.objects.all()
        # 结果返回
        ser = SPUSerializer(spus,many=True)
        return Response(ser.data)