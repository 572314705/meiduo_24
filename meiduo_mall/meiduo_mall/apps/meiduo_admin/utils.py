# 重写jwt，按照后台需求返回结果
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'id':user.id,
    }