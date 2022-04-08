from rest_framework.pagination import LimitOffsetPagination


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 10

# http://127.0.0.1:8000/studentapi/?mylimit=5&myoffset=3
