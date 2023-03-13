from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView


class LCstudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RDUstudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
