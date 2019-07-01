from django.contrib.auth.models import Group
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializer.admins import AdminSerializer
from meiduo_admin.serializer.groups import GroupSerializer
from meiduo_admin.utils import PageNum
from users.models import User


class AdminView(ModelViewSet):
    # 指定序列化器
    serializer_class = AdminSerializer
    # 指定查询集
    queryset = User.objects.filter(is_staff=True)
    # 指定分页器
    pagination_class = PageNum
    # 指定权限
    permission_classes = [IsAdminUser]

    # 获取分组数据
    def simple(self, reqeust):
        pers = Group.objects.all()
        ser = GroupSerializer(pers, many=True)
        return Response(ser.data)