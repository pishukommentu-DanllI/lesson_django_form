from django.urls import path
from . views import *
urlpatterns = [
    path('', index),
    path('appointment', appointment),
    path('task_2', task_2)
]