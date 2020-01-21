from django.urls import path
from timetrack import views

urlpatterns = [
    path('', views.template_login, name='index'),
    path('hello/', views.hello_world),
]
