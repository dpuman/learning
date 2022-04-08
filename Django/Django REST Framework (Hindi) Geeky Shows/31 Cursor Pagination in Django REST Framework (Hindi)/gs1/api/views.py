from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from .mypaginatiot import MyCursorPagination


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination
