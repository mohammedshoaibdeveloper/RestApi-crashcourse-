from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Todo)
admin.site.register(TimingTodo)


################################### Advanced queries #############################``

admin.site.register(Author)
admin.site.register(Book)
