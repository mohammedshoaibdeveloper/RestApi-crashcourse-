from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
# Create your views here.

@api_view(['GET','POST','PATCH','PUT'])
def home(request):

    if request.method == 'GET':

        return Response({'status': 200,'message': 'yes django framework is working',"method":"GET"})

    elif request.method == 'POST':

        return Response({'status': 200,'message': 'yes django framework is working',"method":"POST"})

    elif request.method == 'PATCH':

        return Response({'status': 200,'message': 'yes django framework is working',"method":"PATCH"})

    elif request.method == 'PUT':

        return Response({'status': 200,'message': 'yes django framework is working',"method":"PUT"})

    else:
        return Response({'status': 400,'message': 'yes django framework is working',"method":"you called invalid method"})

@api_view(['GET'])
def get_todo(request):

    todo_obj = Todo.objects.all()
    serializer = TodoSerialzer(todo_obj,many=True)
    return Response({'status': True,'message': 'todo fetched','data':serializer.data})

@api_view(['POST'])
def post_todo(request):
    try:

        data = request.data
        print(data)
        serializer = TodoSerialzer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'success data','data':serializer.data})

        return Response({'status': False,'message': 'invalid data','error':serializer.errors})

    except Exception as e:
        print(e)
        return Response({'status': False,'message': 'something went wrong'})


# done 35 minure 40 seconds