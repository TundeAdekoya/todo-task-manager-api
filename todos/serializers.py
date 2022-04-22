from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Todo


class TodoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Todo
        fields = ('id', 'title', 'manager', 'description', 'start_time', 'end_time', 'task', 'created_on' )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)