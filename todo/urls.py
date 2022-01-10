from django.contrib import admin
from django.urls import path
from .views import CustomObtainAuthToken
from .views import GetNodes
from .views import *

urlpatterns = [
    path('node/', GetNodes.as_view()),
    path('auth/', CustomObtainAuthToken.as_view()),
    path('node_update/<int:pk>', UpdateNodes.as_view()),
    path('register/', registration_view)
]