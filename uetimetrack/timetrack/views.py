from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


# Create your views here.
def hello_world(request):
    return render(request, 'hello_world.html', {})


@login_required
def default_login(request):
    return render(request, 'default_login.html', {})


@login_required
def template_login(request):
    user_group = Group.objects.get(user=request.user).name
    if user_group == 'Student':
        return render(request, 'student_login.html', {})
    elif user_group == 'Student Leader':
        return render(request, 'student_leader_login.html', {})
    elif user_group == 'Advisor':
        return render(request, 'advisor_login.html', {})
    elif user_group == 'Instructor':
        return render(request, 'instructor_login.html', {})
    elif user_group == 'Admin':
        return render(request, 'admin_login.html', {})
    else:
        return render(request, 'hello_world.html', {})
