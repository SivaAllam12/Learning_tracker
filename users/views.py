from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    

    if request.method=='POST':
        print('this is post')
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Hi,'+user+'.  Your profile was created Successfully')
            return redirect('users:login')
    else:
        form=UserCreationForm()
        #print('registration')


    context={'form':form}
    return render(request,'Registration/register.html',context)

def loginfn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(request, username=username, password=password)
        
        if user is not None:
            print('not none')
            login(request, user)
            return redirect('learning_logs:home')
        else:
            messages.info(request,'Username or Password is incorrect. Please try again')
    return render(request,'Registration/login.html')

def logoutUser(request):
    logout(request)
    return redirect('users:login')