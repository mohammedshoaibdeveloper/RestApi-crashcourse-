from django.shortcuts import render,HttpResponse
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
from .protection import *
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



################################### Advanced queries #############################

from home.faker import *

class getData(APIView):

    def post(self, request):

        generate_random_data(n = 5000)
        # generate_data_foriegnkey(n =1000)
        return Response({'status': True,'message': 'generate data successfully'})

    def get(self, request):

        data = Book.objects.all()
        serializer = BookSerialzer(data,many=True)
        return Response({'status': True,'data':serializer.data})

import datetime
from django.db.models import Q
from django.db.models import F
from django.db.models import F, Value as V
from django.db.models.functions import Concat
from django.db.models import Avg, Max, Min
from django.db.models import Count

from django.db.models import F, Q, Value, When, Case
from decimal import Decimal


class AdvancedQuery(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerialzer


    @action(detail=False, methods=['get'])
    def get_book_by_title(self,request):

        objs = Book.objects.filter(title = "Madison King")
        serializer = BookSerialzer(objs,many=True)
        return Response({'status': True,'data':serializer.data})

    
    @action(detail=False, methods=['get'])
    def get_book_by_startwith(self,request):

        objs = Book.objects.filter(title__startswith = "J")
        serializer = BookSerialzer(objs,many=True)
        return Response({'status': True,'data':serializer.data})

    @action(detail=False, methods=['get'])
    def get_book_by_publishedate(self,request):

        # Books published in 2021
        books = Book.objects.filter(published__year=2021)
        # Books published in the year 2000 or after
        books = Book.objects.filter(published__year__gte=2000)
        # # Books published before the year 2000
        # books = Book.objects.filter(published__year__lt=2000)


        serializer = BookSerialzer(books,many=True)
        return Response({'status': True,'data':serializer.data})


    @action(detail=False, methods=['get'])
    def get_book_by_startend_data(self,request):

        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date(2021, 1, 3)
        books = Book.objects.filter(published__range=(start_date, end_date))


        serializer = BookSerialzer(books,many=True)
        return Response({'status': True,'data':serializer.data})

    # Q Objects

    @action(detail=False, methods=['get'])
    def get_book_by_Qobj(self,request):

        # Get all books published in 2018 or 2020
        books = Book.objects.filter(Q(published__year=2018) | Q(published__year=2020))

        serializer = BookSerialzer(books,many=True)
        return Response({'status': True,'data':serializer.data})

    # F expressions

    @action(detail=False, methods=['get'])
    def get_book_f_expression(self,request):

        # Query books published by authors under 30 years old (this is not exactly true because years vary in length)
        books = Book.objects.filter(published__lte=F("author__birth_date") + datetime.timedelta(days=365*30))

        serializer = BookSerialzer(books,many=True)
        return Response({'status': True,'data':serializer.data})


    @action(detail=False, methods=['get'])
    def get_book_f_expression_for_multiple_queies(self,request):

        book = Book.objects.get(title="Timothy Mason Jr.")
        book.update(rating=F("rating") + 1)

        serializer = BookSerialzer(book)
        return Response({'status': True,'data':serializer.data})

    
    # Annotation

    @action(detail=False, methods=['get'])
    def get_book_by_annotate(self,request):

        # author = Author.objects.annotate(full_name=Concat(F("firstname"), V(" "), F("lastname"))).values('nickname','full_name','firstname','lastname','birth_date')

        # Add  a new field with the authors age at the time of publishing the book
        # books = Book.objects.annotate(author_age=F("published") - F("author__birth_date")).values('author_age')
        # Add a new field with the rating multiplied by 100
        books = Book.objects.annotate(rating_multiplied=F("rating") * 100).values('rating_multiplied')

        # serializer = AuthorSerialzer(author)
        return Response({'status': True,'data':books})


    # Aggregation

    @action(detail=False, methods=['get'])
    def get_book_price_by_Aggregation(self,request):

        # result = Book.objects.aggregate(Avg("price"))
        # {'price__avg': Decimal('13.50')}
        # result = Book.objects.aggregate(Max("price"))
        # {'price__max: Decimal('13.50')}
        # result = Book.objects.aggregate(Min("published"))
        # {'published__min': datetime.date(1866, 7, 25)}

        # authors = Author.objects.annotate(num_books=Count("books")).values('books')

        # Calculate average prices for books in all categories.
        book = Book.objects.values("category").annotate(Avg("price"))
        # {'category': 'Historical fiction', 'price__avg': Decimal('13.9900000000000')}, {'category': 'Romance', 'price__avg': Decimal('16.4950000000000')}

     
        return Response({'status': True,'data':book})



    # Case...When

    @action(detail=False, methods=['get'])
    def get_data_case_when(self,request):

        books = Book.objects.annotate(discounted_price=Case(
            When(category="Romance", then=F("price") * Decimal(0.95)),
            When(category="Mystery", then=F("price") * Decimal(0.8)),
            default="price"
        )).values('discounted_price')

        return Response({'status': True,'data':books})


    @action(detail=False, methods=['get'])
    def get_book_select_related(self,request):

        books = Book.objects.select_related("author").all()
        serializer = BookSerialzer(books,many=True)
        return Response({'status': True,'data':serializer.data})


    @action(detail=False, methods=['get'])
    def get_book_prefetch_related(self,request):
        
        authors = Author.objects.prefetch_related("books").all()
        serializer = AuthorSerialzer(authors,many=True)
        return Response({'status': True,'data':serializer.data})


    @action(detail=False, methods=['post'])
    def generatepassword(self,request):
        
        password = request.data['password']
        encryptpassword = hash_password(password)
        print("password-----",encryptpassword)
        return Response({'status': True,'password':password,'encryptpassword':encryptpassword})

    @action(detail=False, methods=['post'])
    def verifypassword(self,request):
        
        encryptpassword = check_password(request.data['password'],request.data['hashed_password'])
        print("encryptpassword",encryptpassword)
        if encryptpassword:
        
            return Response({'status': True,'password':request.data['password'],'encryptpassword':request.data['hashed_password']})

        else:
            return Response({'status': True,"message":"Password not match"})



####################################### Celery #####################################


from .task import *
from .helper import *



def myindex(request):
    # sleep(10)

    # sleepy.delay(30)
    # send_main_without_celery()
    send_mail_task.delay()

    return HttpResponse("<h1>Hello from celery ,</h1>")


############################### redis ################################

from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache


CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)


class getAccounts(APIView):

    def get(self,request):

        checkAccountsExist = cache.get('AccountsData')
        if checkAccountsExist:
            print("cache exist")
            return Response(checkAccountsExist)
        else:

            authorobj = Author.objects.all()
            serializer = AuthorSerialzer(authorobj,many=True)
            message = {'status': True,'data':serializer.data}
            cache.set('AccountsData',message)
            print("not exist")
            return Response(message)



####################### kafka #############################################



from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from .kafka_producer import *
from .kafka_consumer import *


@csrf_exempt
def send_message_to_kafka(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        message = request.POST.get('message')
        send_message(topic, message)
        return HttpResponse('Message sent to Kafka')
    else:
        return HttpResponse('Invalid request method')


def stream_messages_from_kafka(callback, topic):
    def event_stream():
        consume_messages(topic, callback=callback)
        # This line is only reached if consume_messages returns due to an error.
        # If you want to keep the connection open, you can add a retry loop here.
        yield 'Finished consuming messages'

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


@csrf_exempt
def consume_messages_from_kafka(request):
    if request.method == 'GET':
        topic = request.GET['topic']

        def callback(message):
            message_str = message.value().decode('utf-8')
            yield 'data: {}\n\n'.format(message_str)

        return stream_messages_from_kafka(callback, topic)
    else:
        return HttpResponse('Invalid request method')

