from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def hello_world(request):
    return render(request, 'hello_world.html', {})


@login_required
def default_login(request):
    return render(request, 'default_login.html', {})
