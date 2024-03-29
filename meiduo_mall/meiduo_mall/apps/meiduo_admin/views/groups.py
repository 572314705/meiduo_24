from django.contrib.auth.models import Group, Permission
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializer.groups import GroupSerializer
from meiduo_admin.serializer.permission import PermissionSerializer
from meiduo_admin.utils import PageNum


class GroupView(ModelViewSet):
    # 指定序列化器
    serializer_class = GroupSerializer
    # 指定查询集
    queryset = Group.objects.all()
    # 指定分页器
    pagination_class = PageNum
    # 指定权限
    permission_classes = [IsAdminUser]

    # 获取权限表数据
    def simple(self, request):
        # 获取权限
        permission = Permission.objects.all()
        # 序列化返回
        ser = PermissionSerializer(permission, many=True)

        return Response(ser.data)
