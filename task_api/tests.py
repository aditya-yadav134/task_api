from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

# Unit tests for 'Task' Model
class TaskModelTest(TestCase):

  @classmethod
  def setUpTestData(cls):
    test_user = User.objects.create(username="test", password="test2025", first_name='test' )
    Task.objects.create(title='Test task', description='Test description', status= True, owner=test_user)
  
  def test_title_content(self):
    task = Task.objects.get(id=1)
    expected_title = f'{task.title}'
    self.assertEqual(expected_title, 'Test task')

  def test_description_content(self):
     task = Task.objects.get(id=1)
     expected_description = f'{task.description}'
     self.assertEqual(expected_description, 'Test description')

  def test_status(self):
     task = Task.objects.get(id=1)
     expected_status = f'{task.status}'
     self.assertEqual(expected_status, 'True')