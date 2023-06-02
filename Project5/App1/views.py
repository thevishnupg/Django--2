from django.shortcuts import render
from App1.models import Book
from App1.form import BookForm
# Create your views here.


def home(request):
    return render(request,'home.html')

def upload(request):
    objform =BookForm()
    if request.method == "POST":
        objform = BookForm(request.POST)  
        if objform.is_valid():
            objform.save()
            obj2 = Book.objects.all()
            return render(request,'show.html',{'o2':obj2})
        else:
            objform = BookForm()
    return render(request,'upload.html',{'form':objform})


def show(request):
    return render(request,'show.html')

