from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request,"index.html")


def test(request):
    return render(request, "test.html")

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

