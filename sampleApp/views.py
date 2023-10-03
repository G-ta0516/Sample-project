from django.shortcuts import render
from django.http import HttpResponse
from django import forms

def frontpage1(request):
    return render(request,"frontpage1.html")

def registerpage(request):
    return render(request,"register.html")

def submit(request):
    if request.method == 'POST':
        username = request.POST['username']
        userid = request.POST['userid']
        userpass = request.POST['userpass']
        usertype = request.POST['usertype']

        params = {
            "username": username,
            "userid": userid,
            "userpass": userpass,
            "usertype": usertype,
        }
    return render(request,"submit.html",params)