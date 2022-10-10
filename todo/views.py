from msilib.schema import ListView
from multiprocessing import context
from re import template
from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.views.generic.list import ListView

from .forms import TodoForm
from .models import Todo

# Create your views here.
def task(request):
    if request.method == 'POST' :
        Task = TodoForm(request.POST)
        if Task.is_valid():
            Task.save()
            return redirect('list')
    else:
        Task = TodoForm()
        return render(request,'index.html',{'form':Task})

def do(request):
   # todo_items = Todo.objects.all()
    #return render(request, 'list.html',{'todo_items'})
    #model = Todo
    #template_name = "list.html"
    context={}
    context["dataset"] = Todo.objects.all()
    return render(request,'list.html',context)