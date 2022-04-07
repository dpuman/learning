from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer


class StudentList(ListAPIView):
    # queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='user1')
    serializer_class = StudentSerializer

    def get_queryset(self):
        user = self.request.user
        stu = Student.objects.filter(passby=user)
        return stu
