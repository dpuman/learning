from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'stuview'


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'stumodify'


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'stuview'


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'stumodify'


class StudentDelete(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'stumodify'
