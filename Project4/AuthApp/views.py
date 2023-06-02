from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from AuthApp.models import CustomUser,EmployDetail
from AuthApp.form import CustomUserCreationForm
from AuthApp.form import EmployForm

# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def sign1_up(request):
    form = CustomUserCreationForm()
    if (request.method=='POST'):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request, 'sign_up.html',{'form':form})

def log_in(request):
    if (request.method=='POST'):
        name = request.POST['n']
        password = request.POST['p']
        user = authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse('Invalid User')
    return render(request,'log_in.html')

def log_out(request):
    logout(request)
    return log_in(request)


def employ(request):
    if request.method== "POST":
        eid= request.POST['eid']
        ename= request.POST['ename']
        ecom= request.POST['ecom']
        edesig= request.POST['edesig']
        eplace= request.POST['eplace']
        esal= request.POST['esal']

        obj = EmployDetail.objects.create(emp_id=eid,name=ename,company=ecom,designation=edesig,place=eplace,salary=esal)
        obj.save
        
        return render(request,'home.html')
        
    return render(request,'employ.html')

def emp_details(request):

    obj = EmployDetail.objects.all()
    return render(request,'employ_details.html',{'ob':obj})


def view_data(request,p):
    d = EmployDetail.objects.get(pk=p)
    return render(request,'single_employ_details.html',{'data':d})


def edit_data(request,p):
    b = EmployDetail.objects.get(pk=p)
    form = EmployForm(instance=b)
    if request.method == 'POST':
        form = EmployForm(request.POST,instance=b)

        if(form.is_valid()):
            form.save()
            return emp_details(request)
    return render(request,'edit.html',{'form':form})

def delete_data(request,p):
    b = EmployDetail.objects.get(pk=p)
    b.delete()
    return emp_details(request)