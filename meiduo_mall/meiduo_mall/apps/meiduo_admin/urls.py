from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from meiduo_admin.views import admins
from meiduo_admin.views import images
from meiduo_admin.views import orders
from meiduo_admin.views import permission, groups
from meiduo_admin.views import skus
from meiduo_admin.views import specs
from meiduo_admin.views import statistical, users
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # 登录路由
    url(r'^authorizations/$', obtain_jwt_token),
    # ----------数据统计－－－－－－－
    # 用户总数统计
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
    # 日增用户统计
    url(r'^statistical/day_increment/$', statistical.UserDayCountView.as_view()),
    # 日活跃用户统计
    url(r'^statistical/day_active/$', statistical.UserActiveCountView.as_view()),
    # 日下单用户
    url(r'^statistical/day_orders/$', statistical.UserOrderCountView.as_view()),
    # 月增用户
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    # 日分类商品访问量
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayView.as_view()),

    # ----------用户管理－－－－－－－
    url(r'^users/$', users.UserView.as_view()),
    # ----------商品规格表管理管理－－－－－－－
    url(r'^goods/simple/$', specs.SpecsView.as_view({'get': 'simple'})),
    # --------------商品图片表管理--------------
    url(r'^skus/simple/$', images.ImageView.as_view({'get': 'simple'})),
    # --------------SKU表管理--------------
    url(r'^goods/(?P<pk>\d+)/specs/$', skus.SKUViewSet.as_view({'get': 'specs'})),
    # --------------系统权限表管理--------------
    url(r'^permission/content_types/$', permission.PermissionView.as_view({'get': 'content_types'})),
    # --------------用户组管理--------------
    url(r'^permission/simple/$', groups.GroupView.as_view({'get': 'simple'})),
    url(r'^permission/groups/simple/$', admins.AdminView.as_view({'get': 'simple'})),

]
# ----------商品规格表管理管理－－－－－－－
router = DefaultRouter()
router.register(r'goods/specs', specs.SpecsView, base_name='spec')
urlpatterns += router.urls

# --------------商品图片表管理--------------
router = DefaultRouter()
router.register(r'skus/images', images.ImageView, base_name='image')
urlpatterns += router.urls
# --------------SKU表管理--------------
router = DefaultRouter()
router.register(r'skus', skus.SKUViewSet, base_name='skus')

urlpatterns += router.urls

# --------------SKU表管理--------------
router = DefaultRouter()
router.register(r'orders', orders.OrderView, base_name='orders')

urlpatterns += router.urls

# --------------系统权限表管理--------------
router = DefaultRouter()
router.register(r'permission/perms', permission.PermissionView, base_name='perms')

urlpatterns += router.urls

# --------------用户组管理--------------
router = DefaultRouter()
router.register(r'permission/groups', groups.GroupView, base_name='perms')

urlpatterns += router.urls

# -------------管理员用户-------------
router = DefaultRouter()
router.register(r'permission/admins',admins.AdminView,base_name='admins')
urlpatterns += router.urls

