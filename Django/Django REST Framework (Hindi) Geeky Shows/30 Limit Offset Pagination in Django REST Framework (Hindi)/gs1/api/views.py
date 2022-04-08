from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from .mypaginatiot import MyLimitOffsetPagination


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyLimitOffsetPagination

# http://127.0.0.1:8000/studentapi/?limit=5&offset=3
