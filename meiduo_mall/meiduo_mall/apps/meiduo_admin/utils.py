# 重写jwt，按照后台需求返回结果
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'id':user.id,
    }

# 自定义分页器
class PageNum(PageNumberPagination):
    # 前端发送的每页数目关键字名
    page_size_query_param = 'pagesize'
    # 页面最大限制
    max_page_size = 10

    def get_paginated_response(self, data):
        # return Response(OrderedDict([
        # #     ('count', self.page.paginator.count),
        # #     ('next', self.get_next_link()),
        # #     ('previous', self.get_previous_link()),
        # #     ('results', data)
        # # ]))
        return Response({
            'count':self.page.paginator.count,
            'lists':data,
            'page':self.page.number,
            'pages':self.page.paginator.num_pages,
            'pagesize':self.max_page_size,
        })
