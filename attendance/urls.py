from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from attendance.views import index, course, course_detail

router = DefaultRouter()


urlpatterns = [

    path('', index),
    path('course/', course),
    path('course/<int:pk>', course_detail),
]
