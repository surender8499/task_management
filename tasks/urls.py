from django.urls import path
from .views import task_list, task_detail, task_create, task_update

urlpatterns = [
    path('', task_list, name='task-list'),
    path('create/', task_create, name='task-create'),
    path('<int:task_id>/', task_detail, name='task-detail'),
    path('<int:task_id>/update/', task_update, name='task-update'),
]
