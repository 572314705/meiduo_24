from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views.statistical import UserTotalCountView

urlpatterns = [
    # 登录路由
    url(r'^authorizations/$', obtain_jwt_token),
    # 用户总数统计
    url(r'^statistical/total_count/$',UserTotalCountView.as_view())
]