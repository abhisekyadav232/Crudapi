from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class studentviewset(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk):
        id = pk
        if pk is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except:
                return Response({'msg':'data found'})
        
    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data inserted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        id = pk
        try:
            stu = Student.objects.get(id=id)        
            stu.delete()
            return Response({'msg':'data deleted'},status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'Data not found'})
        
