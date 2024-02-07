from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView

# Create your views here.

class TodoListView(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'obj'

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'creat.html'
    success_url = '/'

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'obj'

class TodoUpdateView(UpdateView):
     model = Todo
     template_name = 'update.html'
     fields = '__all__'
     success_url = '/'

class Tododeleteview(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = '/'



    # def index(request):
#     obj = Todo.objects.all()

#     if request.method == 'POST':
#         task = request.POST.get('task')
#         num = request.POST.get('num')
#         dte = request.POST.get('dte')
#         todo = Todo(task=task,number=num,date=dte)
#         todo.save()

#     return render(request,'home.html',{'obj':obj})

# def delt(request,d_id):
#     if request.method == "POST":
#         obj = Todo.objects.get(id=d_id)
#         obj.delete()
#         return redirect('/')
#     return render(request, 'delete.html')

# def update(request,u_id):
#     todoo = Todo.objects.get(id=u_id)
#     todoform = TodoForm(request.POST or None, instance=todoo)

#     if todoform.is_valid():
#         todoform.save()
#         return redirect('/')
#     return render(request, 'update.html',{'form':todoform})