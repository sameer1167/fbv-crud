from django.shortcuts import render, redirect
from fbvApp.models import student
from fbvApp.forms import studentform
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def Liststudent(request):
    studentlist=student.objects.all
    return render(request,'fbv_temp/index.html',{'studentlist':studentlist})


@login_required
def createstudent(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid:
            form.save()
            return Liststudent(request)

    return render(request,'fbv_temp/crud.html',{'form':form})


@login_required
def deletestudent(request,id):
    delstudent=student.objects.get(id=id)
    delstudent.delete()
    return redirect('/')

@login_required
def updatestudent(request,id):
    updstudent=student.objects.get(id=id)
    form=studentform(instance=updstudent)
    if request.method=='POST':
        form=studentform(request.POST,instance=updstudent)
        if form.is_valid:
            form.save()
            return redirect('/')
    return render(request,'fbv_temp/update.html',{'form':form})