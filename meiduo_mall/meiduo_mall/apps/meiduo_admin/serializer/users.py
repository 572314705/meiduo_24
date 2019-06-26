from rest_framework import serializers

from users.models import User

# 自定义一个序列化
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        # 指定根据那个模型类生成序列化器字段
        model = User
        #
        fields =('id','username','mobile','email')
