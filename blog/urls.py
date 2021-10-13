"""


Version: 0.1
Author: 李康
Date: 2021-10-13
"""
from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index')
]