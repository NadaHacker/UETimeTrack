from django.urls import path
from timetrack import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]