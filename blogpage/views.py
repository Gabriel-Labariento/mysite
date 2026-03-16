from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task, TaskGroup, Profile
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


tasks = []

def index(request):
    return HttpResponse("Hello world! This came from the index view.")


def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            tasks.append( (form.cleaned_data['task_name'], form.cleaned_data['task_date']) )
            return redirect('/blogpage/list')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    
    return render(request, "blogpage/task_list.html", {
        'form': form,
        'tasks': tasks,
    })

@login_required
def task_detail(request, id):
    task = Task.objects.get(pk=id)
    return render(request, "blogpage/task_detail.html", {
        "task": task
    })

class TaskAddView(FormView):
    template_name = "blogpage/task_add.html"
    form_class = TaskForm
    success_url = "/blogpage/list"

    def form_valid(self, form):
        tasks.append( (form.cleaned_data['task_name'], form.cleaned_data['task_date']) )
        return super().form_valid(form)


class TaskListView(ListView):
    model = Task
    template_name = 'blogpage/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        context["task_list"] = Task.objects.filter(profile=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
        # Do the Task Creation here, similar to the FBV
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'blogpage/task_detail.html'

    