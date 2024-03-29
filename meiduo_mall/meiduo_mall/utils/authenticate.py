from django.contrib.auth.backends import ModelBackend
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin
from django.http import HttpRequest
import re
from users.models import User


class MeiduoModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 通过判断request对象　前台登录还是后台登录
        if request is None:
            try:
                user = User.objects.get(username=username,is_staff=True)
            except:
                return None
            if user.check_password(password):
                return user
        else:

            try:
                # if re.match(r'^1[3-9]\d{9}$', username):
                #     user = User.objects.get(mobile=username)
                # else:
                #     user = User.objects.get(username=username)
                user = User.objects.get(username=username)
            except:
                # 如果未查到数据，则返回None，用于后续判断
                try:
                    user = User.objects.get(mobile=username)
                except:
                    return None
                    # return None

            # 判断密码
            if user.check_password(password):
                return user
            else:
                return None

