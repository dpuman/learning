from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Generete token from API End cmd
# http POST http://127.0.0.1:8000/gettoken/ username="user3" password="dipankar"

# REQUESTS USING TOKEN BY HTTPIE CMD
# http http://127.0.0.1:8000/studentapi/
# http GET http://127.0.0.1:8000/studentapi/ "Authorization: Token b18f0849e1a8fc9539f370be62108d370d76e051"
# http -f POST http://127.0.0.1:8000/studentapi/ name=Jahid roll=222 city=un "Authorization: Token b18f0849e1a8fc9539f370be62108d370d76e051"
# http PUT http://127.0.0.1:8000/studentapi/16/ name=Shoktiman roll=222 city=un "Authorization: Token b18f0849e1a8fc9539f370be62108d370d76e051"
# http DELETE http://127.0.0.1:8000/studentapi/16/ "Authorization: Token b18f0849e1a8fc9539f370be62108d370d76e051"
