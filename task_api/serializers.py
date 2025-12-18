from rest_framework import serializers
from .models import Task

# Extending 'ModelSerianlizer' for Serializing and Parsing 'Task' model
class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields  = ('id', 'title', 'description', 'status', 'owner')  