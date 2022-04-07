from functools import partial
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        print('*******List*********')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Details', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print('*******Retrieve*********')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Details', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    def create(self, request):
        print('*******Create*********')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Details', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'msg': 'data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        print('*******Update*********')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Details', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'COMPLETE Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        print('*******Partial_update*********')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Details', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'PARTIAL Updated'})
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        print('*******Destroy*********')
        print('Basename', self.basename)
        print('Action', self.action)
        print('Details', self.detail)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'DELEted'})
