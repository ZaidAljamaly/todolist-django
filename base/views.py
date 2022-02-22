from django.shortcuts import render, redirect
##from django.views.generic.list import ListView
from .models import Task
from .form import TaskForm, CreateUserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib import messages


def Login(request):
   if request.user.is_authenticated:
      return redirect('tasks')
   else:
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)

         if user is not None:
            login(request, user)
            return redirect('tasks')
         else:
            messages.info(request, 'Username OR password is incorrect')
   context = {}
   return render(request, 'base/login.html', context)


def Logout(request):
	logout(request)
	return redirect('login')


def registerPage(request):
   form = CreateUserForm
   if request.user.is_authenticated:
      return redirect('tasks')
   else:
      if request.method == 'POST':
         form = CreateUserForm(request.POST)
         if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
   context = {'form': form}
   return render(request, 'base/register.html', context)


@login_required(login_url='login')
def Tasks(request):
   q = request.GET.get('q') if request.GET.get('q') != None else''
   tasks = Task.objects.filter(
       Q(title__icontains=q) |
       Q(description__icontains=q)
   )
   tasksNumber = Task.objects.filter(user=request.user).count()
   context = {'tasks': tasks, 'count': tasksNumber}
   return render(request, 'base/task_list.html', context)


@login_required(login_url='login')
def information(request, pk):
   task = Task.objects.get(id=pk)
   context = {'task': task}
   return render(request, 'base/information.html', context)


def CreateTask(request):
   form = TaskForm
   if request.method == 'POST':
      form = TaskForm(request.POST)
      if form.is_valid():
         task = form.save(commit=False)
         task.user = request.user
         task.save()
         return redirect('tasks')
   context = {'form': form}
   return render(request, 'base/form.html', context)


@login_required(login_url='login')
def UpdateTask(request, pk):
   task = Task.objects.get(id=pk)
   form = TaskForm(instance=task)
   if request.method == 'POST':
       form = TaskForm(request.POST, instance=task)
       if form.is_valid():
          form.save()
          return redirect('tasks')
   context = {'form': form}
   return render(request, 'base/form.html', context)


@login_required(login_url='login')
def DeleteTask(request, pk):
   task = Task.objects.get(id=pk)
   if request.method == 'POST':
      task.delete()
      return redirect('tasks')
   context = {'task': task}
   return render(request, 'base/delete.html', context)
