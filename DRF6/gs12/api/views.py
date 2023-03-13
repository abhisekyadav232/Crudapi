from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView,DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView


class liststudent(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class studentcreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class studentRetrive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class studentupdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class studentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class LCstudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RDstudent(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class RDUstudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
