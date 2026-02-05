from django.urls import path

from .views import *

urlpatterns = [
    path(route='', view=index, name='index'),
    path('list/', task_list, name='task_list')
]

app_name = "blogpage"