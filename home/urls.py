from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo-viewset', TodoViewSet, basename='todo') 
router.register(r'advanced-queries', AdvancedQuery, basename='query') 

urlpatterns = [

 path('',home),
 path('post-todo/',post_todo),
 path('get-todo/',get_todo),
 path('patch-todo/',patch_todo),

 path('todo/',Todos.as_view()),


 path('todo/',Todos.as_view()),

 ################################### Advanced queries #############################
 path('getdata/',getData.as_view()),

 path('myindex/',myindex),
 path('getAccounts/',getAccounts.as_view()),

 path('send_message_to_kafka/',send_message_to_kafka),
 path('consume_messages_from_kafka/',consume_messages_from_kafka),

]
urlpatterns += router.urls

