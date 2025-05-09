from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Task
from django.shortcuts import redirect, get_object_or_404

from django.http import JsonResponse

# Create your views here.



def toggle_star(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_starred = not task.is_starred
    task.save()
    return JsonResponse({'status': 'success', 'is_starred': task.is_starred})



def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user = request.user)
        username = request.user.username
        return render(request, 'index.html', {'tasks': tasks, 'username': username[0]})
    else:
        return render(request, 'login.html')


@login_required                            
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('task')
        note = request.POST.get('note')
        task = Task(title=title, user = request.user, note=note)
        task.save()
    return redirect('index')

def delete_task(request, task_id):
    if request.method == 'POST':
        tsk = Task.objects.get(id=task_id)
        tsk.delete()
        return redirect('index')
    
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else: 
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
    else:
        return render(request, 'login.html')



def abc(request):
    return render(request, 'abc.html')
def favourites(request):
    return render(request, 'favourites.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            return render(request, 'register.html', {'error': "Password do not match"} )
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': "User already exists"})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': "Email already exists"})
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')