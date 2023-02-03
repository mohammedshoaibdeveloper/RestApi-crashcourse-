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
]
urlpatterns += router.urls