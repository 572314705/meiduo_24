from datetime import date, timedelta

from rest_framework import serializers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from goods.models import GoodsVisitCount
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
    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 查询当日活跃用户用户 last_login记录最后登录时间
        count = User.objects.filter(is_staff=False, last_login__gte=now_date).count()
        # 返回结果
        return Response({
            'count': count,
            'date': now_date,
        })


class UserOrderCountView(APIView):
    # 查询日下单用户

    # 指定权限
    permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 查询当日下单用户　关联过滤查询　以订单表数据做为用户表查询条件
        # count = User.objects.filter(is_staff=False,orders__create_time__gte=now_date).count()
        users = User.objects.filter(is_staff=False, orders__create_time__gte=now_date)
        # 下单用户数
        user = set(users)
        count = len(user)

        # 返回结果
        return Response({
            'count': count,
            'date': now_date,
        })


class UserMonthCountView(APIView):
    permission_classes = [IsAdminUser]

    # 月增用户
    def get(self, request):
        # 当天日期
        now_date = date.today()
        # 一个月前的日期
        old_date = now_date - timedelta(30)
        # 一个月的新增用户
        user_date = []
        for i in range(31):
            # 一个月前的日期
            index＿date = old_date + timedelta(i)
            # 一个月前的下一甜日期
            next_date = old_date + timedelta(i + 1)
            count = User.objects.filter(is_staff=False, date_joined__gte=index＿date, date_joined__lt=next_date).count()
            user_date.append({
                'count': count,
                'date': next_date,
            })
        return Response(user_date)

# class GoodsDayView(APIView):
#     # 日商品分类访问量
#     def get(self,request):
#         # 当天日期
#         now_date = date.today()
#         # 获取对象查询集
#         goods = GoodsVisitCount.objects.filter(date=now_date)
#         date_list = []
#         for good in goods:
#             date_list.append({
#                 'count':good.count,
#                 'category':good.category.name,
#             })
#         return Response(date_list)
class GoodsSerializer(serializers.ModelSerializer):
    # 指定返回分类名称
    category=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=GoodsVisitCount
        fields=('count','category')

class GoodsDayView(APIView):

    def get(self,request):
        # 获取当天日期
        now_date=date.today()
        # 获取当天访问的商品分类数量信息
        data=GoodsVisitCount.objects.filter(date=now_date)
        # 序列化返回分类数量
        ser=GoodsSerializer(data,many=True)

        return Response(ser.data)

