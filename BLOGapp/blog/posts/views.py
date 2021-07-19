from django.shortcuts import render,redirect
from .models import blog
from datetime import datetime

# Create your views here.
def index(request):
    post = blog.objects.all()
    return render(request,'index.html',{'post':post})
def read(request,pk):
    read = blog.objects.get(id=pk)
    print(read.Subtitle)
    return render(request,'post.html',{'read':read})

def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        date = datetime.now()
        description = request.POST['description']

        blo = blog.objects.create(title = title,subtitle=subtitle,date=date,description=description)
        blo.save()
        return redirect('index')
    return render(request,'create.html')

def update(request,id):
    pass