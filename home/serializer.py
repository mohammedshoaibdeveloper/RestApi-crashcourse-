from rest_framework import serializers
from .models import *
import re
from django.template.defaultfilters import slugify

class TodoSerialzer(serializers.ModelSerializer):

    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['user','todo_title','slug','todo_description','is_done','uid']

    def get_slug(self,obj):

        return slugify(obj.todo_title)



    def validate_todo_title(self,data):
        if data:
            todo_title = data
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

            if len(todo_title) < 3:
                raise serializers.ValidationError('todo title must be more than 3 characters')

            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('todo title cannot contain special characters')
            
        return data


class TimingTodoSerializer(serializers.ModelSerializer):

    todo = TodoSerialzer()

    class Meta:
        model = TimingTodo
        exclude = ['created_at', 'updated_at']
        # depth =1


    
    # def validate(self,validated_data):

    #     if validated_data.get('todo_title'):
    #         todo_title = validated_data['todo_title']
    #         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    #         if len(todo_title) < 3:
    #             raise serializers.ValidationError('todo title must be more than 3 characters')

    #         if not regex.search(todo_title) == None:
    #             raise serializers.ValidationError('todo title cannot contain special characters')
            
    #         return validated_data




