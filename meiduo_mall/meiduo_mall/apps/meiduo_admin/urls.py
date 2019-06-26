from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views import statistical

urlpatterns = [
    # 登录路由
    url(r'^authorizations/$', obtain_jwt_token),
    # 用户总数统计
    url(r'^statistical/total_count/$',statistical.UserTotalCountView.as_view()),
    # 日增用户统计
    url(r'^statistical/day_increment/$',statistical.UserDayCountView.as_view()),
    # 日活跃用户统计
    url(r'^statistical/day_active/$',statistical.UserActiveCountView.as_view()),
]