from functools import partial
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request, id=None):

    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'msg': 'data Created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Updated'})
        return Response(serializer.errors)
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'DELEted'})

# def student_api(request):
# if request.method == 'GET':
#     json_data = request.body
#     stream_data = io.BytesIO(json_data)
#     parsed_data = JSONParser().parse(stream_data)
#     id = parsed_data.get('id', None)
#     if id is not None:
#         student = Student.objects.get(pk=id)
#         student_serializer = StudentSerializer(student)
#         student_json = JSONRenderer().render(student_serializer.data)
#         print(student_json)
#         return HttpResponse(student_json, content_type='application/json')
#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu, many=True)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

# if request.method == 'POST':
#     json_data = request.body

#     stream_data = io.BytesIO(json_data)
#     parsed_data = JSONParser().parse(stream_data)

#     serialized_data = StudentSerializer(data=parsed_data)
#     if serialized_data.is_valid():
#         serialized_data.save()
#         msg = {'success': 'saved Data'}
#         return JsonResponse(msg)
#     json_data = JSONRenderer().render(serialized_data.errors)
#     return HttpResponse(json_data, content_type='application/json')
# if request.method == 'PUT':
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     pythondata = JSONParser().parse(stream)
#     id = pythondata.get('id')
#     stu = Student.objects.get(id=id)

#     serializer = StudentSerializer(stu, data=pythondata, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         msg = {'success': 'Updated Data'}
#         return JsonResponse(msg)
#     json_data = JSONRenderer().render(serializer.errors)
#     return HttpResponse(json_data, content_type='application/json')
# if request.method == 'DELETE':
#     json_data = request.body
#     stream = io.BytesIO(json_data)
#     pythondata = JSONParser().parse(stream)
#     id = pythondata.get('id')
#     stu = Student.objects.get(id=id)
#     stu.delete()

#     res = {
#         'msg': 'Data Deleted'
#     }
#     json_data = JSONRenderer().render(res)
#     return HttpResponse(json_data, content_type='application/json')
