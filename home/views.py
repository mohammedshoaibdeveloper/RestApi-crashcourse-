from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from django.core.paginator import Paginator
from .helper import *
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

@api_view(['PATCH'])
def patch_todo(request):

    try:
        data = request.data
        if not data.get('uid'):

            return Response({'status': False,'message': 'uid is required','data':{}})


        obj = Todo.objects.get(uid = data.get('uid'))
        serializers = TodoSerialzer(obj,data = data,partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'status': True,'message': 'success data','data':serializers.data})

        return Response({'status': False,'message': 'invalid data','error':serializers.errors})

    except Exception as e:
        print(e)
        return Response({'status': False,'message': 'invalid uid','data':{}})


class Todos(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        # print(request.user)

        # todo_obj = Todo.objects.filter(user = request.user)
        # serializer = TodoSerialzer(todo_obj,many=True)
        # return Response({'status': True,'message': 'todo fetched','data':serializer.data})


        #################### pagination #################

        

        todo_obj = Todo.objects.filter(user = request.user)
        page = request.GET.get('page',1)
        page_obj = Paginator(todo_obj, page)
        results = paginate(todo_obj,page_obj,page)
        # print(results)

        serializer = TodoSerialzer(results['results'],many=True)
        return Response({'status': True,'message': 'todo fetched','data':{'data':serializer.data,'pagination':results['pagination']}})

    def post(self, request):

        # try:
        data = request.data
        data['user'] = request.user.id
        print(data)
        serializer = TodoSerialzer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True,'message': 'success data','data':serializer.data})

        return Response({'status': False,'message': 'invalid data','error':serializer.errors})

        # except Exception as e:
        #     print(e)
        #     return Response({'status': False,'message': 'something went wrong'})

    def patch(self, request):

        try:
            data = request.data
            if not data.get('uid'):

                return Response({'status': False,'message': 'uid is required','data':{}})


            obj = Todo.objects.get(uid = data.get('uid'))
            serializers = TodoSerialzer(obj,data = data,partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response({'status': True,'message': 'success data','data':serializers.data})

            return Response({'status': False,'message': 'invalid data','error':serializers.errors})

        except Exception as e:
            print(e)
            return Response({'status': False,'message': 'invalid uid','data':{}})


    def put(self, request):

        return Response({'status': 200,'message': 'yes django framework is working',"method":"PUT"})

    def delete(self, request):

        return Response({'status': 200,'message': 'yes django framework is working',"method":"delete"})


from rest_framework.decorators import action


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerialzer

    #agr detail=False hoga to iska mtlb ye hy k hm paranerter mn koi chz pass nhi krrhe for example agr hm ko slug pass krna hy to isko true krna prega or wo chz is action se phle pass krni pregi

    @action(detail=False, methods=['get'])
    def get_timing_to_todo(self,request):

        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs,many=True)
        return Response({'status': True,'message': 'timing todo fetched','data':serializer.data})


    @action(detail=False, methods=['post'])
    def add_data_to_todo(self,request):

        try:

            data = request.data
            serializer = TimingTodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True,'message': 'success data','data':serializer.data})

            return Response({'status': False,'message': 'invalid data','error':serializer.errors})


        
        except Exception as e:
            print(e)
            return Response({'status': False,'message': 'invalid uid','data':{}})
        



# https://github.com/boxabhi
# https://github.com/boxabhi/enginee_babu_authenticate/blob/main/base_rest/utils.py