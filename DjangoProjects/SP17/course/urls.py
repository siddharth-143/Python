from django.urls import path
from . import views
urlpatterns = [
    path('learndj/', views.learn_django, name='courseone'),
    path('learnpy/', views.learn_python, name='courseone'),
]
