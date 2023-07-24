from django.shortcuts import render

def frontpage(request):
    return render(request,"frontpage.html")

def registerpage(request):
    return render(request,"register.html")