from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),


    path('home', ToDo.as_view(), name='todo'),
    path('task/', TaskList.as_view(), name='tasks'),
    path('task-create/', CreateTask.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', DeleteTask.as_view(), name='task-delete'),
    path('pending/', Pending.as_view(), name='pending'),
    path('complete/', Complete.as_view(), name='complete'),
]
