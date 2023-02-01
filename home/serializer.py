from rest_framework import serializers
from .models import *
import re


class TodoSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['todo_title','todo_description','is_done','uid']

    
    def validate(self,validated_data):

        if validated_data.get('todo_title'):
            todo_title = validated_data['todo_title']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('todo title cannot contain special characters')
            
            return validated_data




