from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
# from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def HomeView(request):
    return render(request,'tasks/mainhome.html',{})

@login_required(login_url="login")
def index(request):
    profil=request.user.profile
    print(profil.id)
    # mid=Middle.objects.get_or_create(profile=profile.id)
    # print(mid)
    tasks=Task.objects.filter(profile=profil)
    print(tasks)
    form=TaskForm()
    if request.method=='POST':
        # print(request.POST)
        form=TaskForm(request.POST)
        
        if form.is_valid():
            # print(form.cleaned_data)
            # print(form.profile)
            fake=form.save(commit=False)
            fake.profile=profil
            fake.save()
        return redirect('list') 
    
    context={'tasks':tasks,'form':form}
    return render(request,'tasks/list.html',context)

@login_required(login_url="login")
def UpdateTask(request,pk):
    task=get_object_or_404(Task,id=pk)

    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
    context={'form':form}
    return render(request,'tasks/update_task.html',context)
@login_required(login_url="login")
def deleteTask(request,pk):
    item=get_object_or_404(Task,id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('list')
    context={'item':item}
    return render(request,'tasks/delete.html',context)    

def LoginView(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:    
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('list')
            else:
                messages.info(request,'Wrong password or Username')    

        context={}
        return render(request,'tasks/login.html',context)

def RegisterView(request):
    if request.user.is_authenticated:
        return redirect('list')
    else:    
        form=UserForm()
        if request.method=='POST':
            form=UserForm(request.POST)
            if form.is_valid():
                user=form.save()
                username=form.cleaned_data.get('username')
                messages.success(request,'User created for'+username)
                Profile.objects.create(
                    user=user,
                    name=user.username,
                    # email=user.email
                )
                
                return redirect('home')
        context={'form':form}
        return render(request,'tasks/register.html',context)   

@login_required(login_url="login")
def LogoutView(request):
    logout(request)
    return redirect('home')             