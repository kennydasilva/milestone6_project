from django.urls import path
from .views import healt_check

urlpatterns=[
    path('healt/', healt_check),
]