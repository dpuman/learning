from rest_framework.pagination import CursorPagination


class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'cu'

# http://127.0.0.1:8000/studentapi/?cu=cj0xJnA9RGlwYW5rYXI%3D
