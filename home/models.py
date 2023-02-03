from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


class BaseModel(models.Model):

    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Todo(BaseModel):
    
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank = True,null = True)
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False)


class TimingTodo(BaseModel):

    todo = models.ForeignKey(Todo,on_delete=models.CASCADE)
    timing = models.DateField()



################################### Advanced queries #############################``


class Author(models.Model):
    nickname = models.CharField(max_length=20, null=True, blank=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=40)
    birth_date = models.DateField()

    
class Book(models.Model):
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=100)
    category = models.CharField(max_length=50)
    published = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    rating = models.IntegerField()

