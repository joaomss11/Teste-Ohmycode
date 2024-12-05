from django.urls import path
from .views import TasksAPIView, TaskAPIView, UserAPIView, UsersAPIView, CurrentUserTasks

urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users'),
    path('users/<int:pk>', UserAPIView.as_view(), name='user'),
    #path('users/<int:user_pk>/tasks/', TasksAPIView.as_view(), name='user_tasks'),
    path('users/tasks', CurrentUserTasks.as_view(), name='user_tasks'),
    #path('users/<int:user_pk>/tasks/<int:task_pk>', TaskAPIView.as_view(), name='user_task'),
    path('tasks/', TasksAPIView.as_view(), name='tasks'),
    path('tasks/<int:pk>', TaskAPIView.as_view(), name='task')   
]
