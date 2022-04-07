from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.


def student_details(request, id):
    student = Student.objects.get(pk=id)
    print(student)
    student_serializer = StudentSerializer(student)
    print(student_serializer)
    print(student_serializer.data)
    student_json = JSONRenderer().render(student_serializer.data)
    print(student_json)
    return HttpResponse(student_json, content_type='application/json')


# def students(request):
#     students = Student.objects.all()
#     print(students)

#     students_serializer = StudentSerializer(students, many=True)
#     print(students_serializer)
#     print(students_serializer.data)

#     students_json = JSONRenderer().render(students_serializer.data)
#     print(students_json)

#     return HttpResponse(students_json, content_type='application/json')

# using JSONResponse
def students(request):
    students = Student.objects.all()
    print(students)

    students_serializer = StudentSerializer(students, many=True)
    print(students_serializer)
    print(students_serializer.data)

    return JsonResponse(students_serializer.data, safe=False)
