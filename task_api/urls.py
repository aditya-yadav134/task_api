from django.urls import path, include
from .views import DetailTask, ListTask

urlpatterns = [
    # Path for individual Tasks
    path('<int:pk>/', DetailTask.as_view(), name='detail_view'),

    # Path to display all Tasks
    path('', ListTask.as_view(), name='list_view'),
]