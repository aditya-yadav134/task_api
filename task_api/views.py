from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAdminOrOwner

class ListTask(generics.ListCreateAPIView):
  serializer_class  = TaskSerializer

  # If Admin return all tasks or tasks of current User 
  def get_queryset(self):
      if self.request.user.is_staff:
        return Task.objects.all()
      else:
        return Task.objects.filter(owner= self.request.user)

class DetailTask(generics.RetrieveUpdateDestroyAPIView):
  queryset  = Task.objects.all()
  serializer_class  = TaskSerializer

  # Permission class Allowing only Admin or Owner of task for accessing view
  permission_classes = (IsAdminOrOwner,)
