from datetime import date

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from users.models import User
from rest_framework.views import APIView


class UserTotalCountView(APIView):
    # 用户总数统计
    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 获取用户总数
        count = User.objects.filter(is_staff=False).count()
        # 返回结果
        return Response({
            'count': count,
            'date': now_date,
        })


class UserDayCountView(APIView):
    # 日增用户统计
    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 查询当日新增用户
        count = User.objects.filter(is_staff=False, date_joined__gte=now_date).count()
        # 返回结果
        return Response({
            'count': count,
            'date': now_date,
        })

class UserActiveCountView(APIView):
    # 查询日活跃用户
    def get(self,request):
        # 获取当前日期
        now_date = date.today()
        # 查询当日活跃用户用户 last_login记录最后登录时间
        count = User.objects.filter(is_staff=False,last_login__gte=now_date).count()
        # 返回结果
        return Response({
            'count':count,
            'date':now_date,
        })
class UserOrderCountView(APIView):
    # 查询日下单用户

    # 指定权限
    permission_classes = [IsAdminUser]
    def get(self,request):
        # 获取当前日期
        now_date = date.today()
        # 查询当日下单用户　关联过滤查询　以订单表数据做为用户表查询条件
        count = User.objects.filter(is_staff=False,orders__create_time__gte=now_date).count()
        # 返回结果
        return Response({
            'count':count,
            'date':now_date,
        })