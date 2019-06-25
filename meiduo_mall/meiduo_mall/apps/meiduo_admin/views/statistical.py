from datetime import date

from rest_framework.response import Response

from users.models import User
from rest_framework.views import APIView


class UserTotalCountView(APIView):
    # 用户总数统计
    def get(self,request):
        # 获取当前日期
        now_date = date.today()
        # 获取用户总数
        count = User.objects.filter(is_staff=False).count()
        # 返回结果
        return Response({
            'count':count,
            'date':now_date,
        })
