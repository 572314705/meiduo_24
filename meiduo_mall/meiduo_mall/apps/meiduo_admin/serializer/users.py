import re
from rest_framework import serializers

from users.models import User


# 自定义一个序列化
class UserSerializer(serializers.ModelSerializer):
    """
           用户序列化器 ModelSerializer帮助实现了create和update方法
       """

    class Meta:
        # 指定根据那个模型类生成序列化器字段
        model = User
        #
        fields = ('id', 'username', 'mobile', 'email', 'password')
        # username字段增加长度限制，password字段只参与保存，不在返回给前端，增加write_only选项参数
        extra_kwargs = {
            'password': {
                'write_only': True,
                'max_length': 20,
                'min_length': 8,
            },
            'username': {
                'max_length': 20,
                'min_length': 5,
            }
        }

    def validate_mobile(self, value):
        """
            手机号验证
        :param attrs:
        :return:
        """
        if not re.match(r'1[3-9]\d{9}', value):
            raise serializers.ValidationError('手机格式不正确')
        return value

    def create(self, validated_data):
        # user = super().create(validated_data)
        # user.set_password(validated_data['password'])
        # user.save()

        user = User.objects.create_user(**validated_data)

        return user