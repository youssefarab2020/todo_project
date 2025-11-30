from django.shortcuts import render ,redirect
from .models import Task

# Create your views here.
def home(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:  # فقط إذا كان هناك نص
            Task.objects.create(title=title)
        return redirect('/')  # بعد الإضافة نرجع للصفحة الرئيسية

    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def addTask(request):
    if request.method=="POST":
        title=request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('/')
    return render(request,'tasks.html')

def deleteTask(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('/')

def updateTask(request,id):
    task=Task.objects.get(id=id)
    if request.method=="POST":
        task.title=request.POST.get('title')
        task.save()
        return redirect('/')
    return render(request,"update_task.html",{'task':task})
