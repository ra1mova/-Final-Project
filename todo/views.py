from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST


def index(request):
    todo = Todo.objects.order_by('id')
    form = TodoForm()
    return render(request, 'index.html', {'todo_list': todo, 'form': form})


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('/')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.complete:
        todo.complete = False
        todo.save()
    else:
        todo.complete = True
        todo.save()
    return redirect('index')


def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()
    return redirect('index')
