from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'title':'Curso de Django'
    })

def hello(request, id):
    result = id + 100 * 2
    return HttpResponse("<h2>Hello %s<h2>" % result)     

def about(request):
    return render(request, 'about.html')


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })
    
def task(request, title):
    task = Task.objects.get(title = title)
    return HttpResponse(task)

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask()  
    })
    else:
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description, project_id=1)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
        'form': CreateNewProject()  
    })
    else:
        title = request.POST['title']
        Project.objects.create(name=title)
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })