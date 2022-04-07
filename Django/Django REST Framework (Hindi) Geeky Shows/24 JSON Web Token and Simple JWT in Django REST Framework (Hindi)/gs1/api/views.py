from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAuthenticated]


# Generete token from API End cmd
# http POST http://127.0.0.1:8000/gettoken/ username="user1" password="dipankar"
# http POST http://127.0.0.1:8000/verifytoken/ token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ5MjE5OTUwLCJpYXQiOjE2NDkyMTg0NTAsImp0aSI6IjU1NTg2NmVmMGY4NzQ1MjY4ZGI3MWViYjgzYTlmMDUyIiwidXNlcl9pZCI6Mn0.3Elvmyv-7zsGLOQbWlvvJ4YuOY8zZcDpAlFQViw12vw"
# http POST http://127.0.0.1:8000/refreshtoken/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0OTMwNDg1MCwiaWF0IjoxNjQ5MjE4NDUwLCJqdGkiOiJmNzFjNWNhNDQ5ZmQ0OTdhOWMyZGNhOTk1NDYzZDNlMSIsInVzZXJfaWQiOjJ9.0hCflx2TsNcFfr45qjZcGo1JNiUDef19R9pUdt6yTtI"

# REQUESTS USING TOKEN BY HTTPIE CMD
# http http://127.0.0.1:8000/studentapi/

# http GET http://127.0.0.1:8000/studentapi/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ5MjIwMjMyLCJpYXQiOjE2NDkyMTg0NTAsImp0aSI6ImQ2ODRjZGQ3Y2U4NzQ4ZDRiYzM1MTRmYjA5ZWRjZTM3IiwidXNlcl9pZCI6Mn0.ticCgD1v5YLDQ2BnuvNmWC-MibPRqVoHMhJDxcq3lhc"

# http -f POST http://127.0.0.1:8000/studentapi/ name=Jahid roll=222 city=un "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ5MjIwMjMyLCJpYXQiOjE2NDkyMTg0NTAsImp0aSI6ImQ2ODRjZGQ3Y2U4NzQ4ZDRiYzM1MTRmYjA5ZWRjZTM3IiwidXNlcl9pZCI6Mn0.ticCgD1v5YLDQ2BnuvNmWC-MibPRqVoHMhJDxcq3lhc"

# http PUT http://127.0.0.1:8000/studentapi/16/ name=Shoktiman roll=222 city=un "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ5MjIwMjMyLCJpYXQiOjE2NDkyMTg0NTAsImp0aSI6ImQ2ODRjZGQ3Y2U4NzQ4ZDRiYzM1MTRmYjA5ZWRjZTM3IiwidXNlcl9pZCI6Mn0.ticCgD1v5YLDQ2BnuvNmWC-MibPRqVoHMhJDxcq3lhc"

# http DELETE http://127.0.0.1:8000/studentapi/16/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ5MjIwMjMyLCJpYXQiOjE2NDkyMTg0NTAsImp0aSI6ImQ2ODRjZGQ3Y2U4NzQ4ZDRiYzM1MTRmYjA5ZWRjZTM3IiwidXNlcl9pZCI6Mn0.ticCgD1v5YLDQ2BnuvNmWC-MibPRqVoHMhJDxcq3lhc"


'''
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ5MjE5OTUwLCJpYXQiOjE2NDkyMTg0NTAsImp0aSI6IjU1NTg2NmVmMGY4NzQ1MjY4ZGI3MWViYjgzYTlmMDUyIiwidXNlcl9pZCI6Mn0.3Elvmyv-7zsGLOQbWlvvJ4YuOY8zZcDpAlFQViw12vw",

    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0OTMwNDg1MCwiaWF0IjoxNjQ5MjE4NDUwLCJqdGkiOiJmNzFjNWNhNDQ5ZmQ0OTdhOWMyZGNhOTk1NDYzZDNlMSIsInVzZXJfaWQiOjJ9.0hCflx2TsNcFfr45qjZcGo1JNiUDef19R9pUdt6yTtI"

    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ5MjIwMjMyLCJpYXQiOjE2NDkyMTg0NTAsImp0aSI6ImQ2ODRjZGQ3Y2U4NzQ4ZDRiYzM1MTRmYjA5ZWRjZTM3IiwidXNlcl9pZCI6Mn0.ticCgD1v5YLDQ2BnuvNmWC-MibPRqVoHMhJDxcq3lhc"
    
'''
