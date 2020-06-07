from django.shortcuts import render, redirect
from .models import Course
from .models import Entry
from .forms import Courseform
from .forms import Entryform
from django.contrib.auth.decorators import login_required
import requests


def home(request):
    return render(request,'homepage.html')

@login_required(login_url='users:login')
def courses(request):
    courses=Course.objects.filter(owner=request.user)
    context={'courses':courses}
    return render(request,'coursespage.html',context)

@login_required(login_url='users:login')
def addcourse(request):
    if request.method != 'POST':
        
        #print(request.method)
        form=Courseform()
    else:
        form=Courseform(request.POST)
        if form.is_valid():
            newform=form.save(commit=False)
            newform.owner=request.user
            newform.save()

            return redirect('learning_logs:courses')
    context={'form':form}
    return render(request,'addcourse.html',context)

@login_required(login_url='users:login')
def entrypage(request, cid):
    course=Course.objects.get(id=cid)
    entries=course.entry_set.all()
    context={'entries':entries,'cid':cid,'course':course}
    return render(request,'entrypage.html',context)

def entries(request):
    date=request.POST['Date']
    entries=Entry.objects.filter(Date=date)
    context={'entries':entries,'date':date}
    return render(request, 'dateentries.html', context)

@login_required(login_url='users:login')
def deletecourse(request, cid):
    course=Course.objects.get(id=cid)
    if request.method=='POST':
        course.delete()
        return redirect('learning_logs:courses')
    else:
        context={'cid':cid}
        return render(request,'deletecourse.html',context)

@login_required(login_url='users:login')
def addentry(request, cid):
    if request.method != 'POST':
        course=Course.objects.get(id=cid)
        #print(request.method)
        form=Entryform()
    else:
        form=Entryform(request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.course_name=Course.objects.get(id=cid)
            new_entry.save()
            return redirect('learning_logs:entrypage',cid)
    context={'form':form,'cid':cid}
    return render(request,'addentry.html',context)

def covid19(request):
    url='https://api.covid19india.org/data.json'
    r=requests.get(url)
    if r.status_code==200:
        data=r.json()
        indian_cases=data['cases_time_series']
        andhra_cases=data['statewise']
        indian_active=int(indian_cases[-1]['totalconfirmed'])-int(indian_cases[-1]['totalrecovered'])
        context={'indian_cases':indian_cases[-1],'andhra_cases':andhra_cases,'indian_active':indian_active}
        return render(request,'covid19.html',context)
