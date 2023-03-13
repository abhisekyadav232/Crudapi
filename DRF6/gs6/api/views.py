from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'hello world'})

# @api_view()
# def hello_world(request):
#     return Response({'msg':'hello world'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({'This is post method'})

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg':'thai is Get Method'})
    if request.method == 'POST':
        return Response({'msg':'This is post method','data':request.data})
