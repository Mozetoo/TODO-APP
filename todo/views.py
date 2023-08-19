from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import LoginForm, CustomUserCreationForm


# Create your views here.

class LogIn(LoginView):
    template_name = 'cred/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo')


class SignUpView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'cred/signup.html'  # Replace 'your_template_name.html' with your actual template path
    success_url = reverse_lazy('login')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo')
        return super(SignUpView, self).get(*args, **kwargs)


class ToDo(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasksd'
    template_name = 'todo/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasksd'] = context['tasksd'].filter(user=self.request.user)
        context['count'] = context['tasksd'].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasksd'] = context['tasksd'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasksd'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasksd'] = context['tasksd'].filter(user=self.request.user)
        context['count'] = context['tasksd'].filter(completed=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasksd'] = context['tasksd'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('tasks')


class Pending(LoginRequiredMixin, ListView):
    template_name = 'todo/pending.html'
    context_object_name = 'tasksd'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user, completed=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_task_count'] = context['tasksd'].count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasksd'] = context['tasksd'].filter(
                title__contains=search_input)

        context['search_input'] = search_input
        return context


class Complete(LoginRequiredMixin, ListView):
    template_name = 'todo/complete.html'
    context_object_name = 'tasksd'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user, completed=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['completed_task_count'] = context['tasksd'].count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasksd'] = context['tasksd'].filter(
                title__contains=search_input)

        context['search_input'] = search_input
        return context
