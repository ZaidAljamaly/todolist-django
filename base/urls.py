from django.urls import path
from . import views
urlpatterns = [
    path('', views.Tasks, name='tasks'),
    path('task/<str:pk>', views.information, name='task'),
    path('form/', views.CreateTask, name='form'),
    path('task-update/<str:pk>', views.UpdateTask, name='task-update'),
    path('task-delete/<str:pk>', views.DeleteTask, name='task-delete'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.registerPage, name='register'),
]
