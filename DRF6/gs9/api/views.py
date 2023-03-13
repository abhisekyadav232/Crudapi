from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class StudentApi(APIView):
    def get(self,request,pk = None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            if stu is not None:
                serializer = StudentSerializer(stu)
                print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',serializer)
                return Response(serializer.data)                                                
            return Response({'msg':'Data not found'},status=status.HTTP_400_BAD_REQUEST)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data inserted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None,format=None):  
        
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None,format=None):
        
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg':'data deleted'},status=status.HTTP_200_OK)

        