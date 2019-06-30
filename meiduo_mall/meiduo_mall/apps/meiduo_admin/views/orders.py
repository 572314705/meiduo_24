from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet

from meiduo_admin.serializer.orders import OrderSerializer
from meiduo_admin.utils import PageNum
from orders.models import OrderInfo


class OrderView(ReadOnlyModelViewSet):
    # 指定序列化器
    serializer_class = OrderSerializer
    # 指定分页器
    pagination_class = PageNum
    # 指定权限
    permission_classes = [IsAdminUser]

    # 重写get_queryset方法，
    def get_queryset(self):
        # 1、获取前端的keyword参数
        keyword = self.request.query_params.get('keyword')
        if keyword == '' or keyword == None:
            return OrderInfo.objects.all()
        else:
            return OrderInfo.objects.filter(order_id__contains=keyword)
