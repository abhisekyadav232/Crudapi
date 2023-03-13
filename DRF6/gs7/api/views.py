from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET','POST', 'PUT', 'DELETE','PATCH'])
def studentApi(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            print(stu)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ({'msg': 'Data inserted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    if request.method == 'PUT':
        # id = request.data.get('id')
        id=pk
        stu = Student.objects.get(pk=id)
       
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data updated'},status=status.HTTP_202_ACCEPTED)
        return Response((serializer.errors),status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        # id = request.data.get('id')
        id=pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'Data deleted'})