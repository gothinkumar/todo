from django.urls import path
from . import views
from .views import TodoListView,TodoDetailView,TodoUpdateView,Tododeleteview,TodoCreateView
app_name = 'todoapp'

urlpatterns = [

    path('',views.TodoListView.as_view(), name='home'),
    path('detail/<pk>/',views.TodoDetailView.as_view(), name='detail'),
    path('update/<pk>/', views.TodoUpdateView.as_view(), name='update'),
    path('delete/<pk>/',views.Tododeleteview.as_view(), name='delete'),
    path('create/',views.TodoCreateView.as_view(), name='create'),
]
