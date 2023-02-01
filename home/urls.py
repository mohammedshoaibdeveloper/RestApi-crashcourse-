from .views import *
from django.urls import path

urlpatterns = [

 path('',home),
 path('post-todo/',post_todo),
 path('get-todo/',get_todo),
]