from django.db.models.query import QuerySet
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from films.utils import get_max_order, reorder

from films.forms import RegisterForm
from films.models import Task , UserTasks
# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
class Login(LoginView):
    template_name = 'registration/login.html'

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)

class TasksView(ListView):
    template_name = 'tasks.html'
   
    model = Task
    
    context_object_name = 'tasks'
    
    def get_queryset(self):
        user = self.request.user
        
        return UserTasks.objects.filter(user=self.request.user)
#
# ´move HTMX views to another file


#@login_required
def add_task(request):
    name = request.POST.get('taskName')
    
    # add task
    task = Task.objects.get_or_create(taskName=name)[0]

    # add the film to the user's list
    if not UserTasks.objects.filter(task=task, user=request.user).exists():
        UserTasks.objects.create(
            task=task, 
            user=request.user, 
            order=get_max_order(request.user)
        )

    # return template fragment with all the user's films
    tasks = UserTasks.objects.filter(user=request.user)
    messages.success(request, f"Added {name} to list of tasks")
    return render(request, 'partials/task-list.html', {'tasks': tasks})
"""    # add the task to the user's list
    request.user.tasks.add(task)

    # return template fragment with all the user's tasks
    tasks = request.user.tasks.all()
    messages.success(request, 'Added {name} to list of tasks')
    return render(request, 'partials/task-list.html', {'tasks': tasks})"""


#@login_required
#@require_http_methods(["DELETE"])
def delete_task(request, pk):
    # remove the task from the user's list
    request.user.tasks.remove(pk)

    # return template fragment with all the user's tasks
    tasks = request.user.tasks.all()
    return render(request, 'partials/task-list.html', {'tasks': tasks})

def search_task(request):
    search_text = request.POST.get('search')
    usertasks = request.yser.tasks.all()
    
    results = Task.objects.filter(name_contains=search_text).exclude(name__in=usertasks.values_list('name', flat=True))
    context = {'results': results}
    return render(request, 'partials/search-results.html', context)


def check_username(request):
    print("test")
    username = request.POST.get('username')
    print("testtest")
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<div id="username-err" class="error"> This username already exists</div>')
    else:
        return HttpResponse('<div id="username-err" class="success"> This username is available</div>')


def clear(request):
    return HttpResponse("")

def sort(request):
    task_pks_order = request.POST.getlist('task_order')
    tasks = []
    for idx, task_pk in enumerate(task_pks_order, start=1):
        task = Task.objects.get(pk=task_pk)
        task.order = idx
        task.save()
        tasks.append(task)

    return render(request, 'partials/task-list.html', {'tasks': tasks})
