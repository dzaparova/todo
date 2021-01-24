from django.shortcuts import render, HttpResponse
from.models import ToDo, Book

def homepage(request):
    return render(request,"index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list":todo_list})

def second(request):
    return HttpResponse("test2page")

def third(request):
    return HttpResponse("This is page test3")

def index1(request):
    return render(request, "index1.html")

def index2(request):
    return render(request, "index2.html")

def index3(request):
    return render(request, "index3.html")

def books(request): 
    books = Book.objects.all()
    return render(request, "books.html" , {"books" : books})
    


