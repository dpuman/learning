import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def createStudent(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        stream_data = io.BytesIO(json_data)
        parsed_data = JSONParser().parse(stream_data)

        serialized_data = StudentSerializer(data=parsed_data)
        if serialized_data.is_valid():
            serialized_data.save()
            msg = {'success': 'saved Data'}
            return JsonResponse(msg)
        json_data = JSONRenderer().render(serialized_data.errors)
        return HttpResponse(json_data, content_type='application/json')
