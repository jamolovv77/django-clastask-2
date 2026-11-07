from django.urls import  path
from.views import *

urlpatterns = [
    path('a', home_task),
    path('b',profile_task),
    path('c',sadi_task),
    path('d',wirinwoh_task)
]
