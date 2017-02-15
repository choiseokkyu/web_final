from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "index.html")
def introduce(request):
    return render(request, "introduce.html")
def main(request):
    return render(request, "main.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request,"contact.html")
def project(request):
    return render(request,"main.html")
def project1(request):
    return render(request,"project1.html")
def project2(request):
    return render(request,"project2.html")
def project3(request):
    return render(request,"project3.html")
def project4(request):
    return render(request,"project4.html")
def project5(request):
    return render(request,"project5.html")
def project6(request):
    return render(request,"project6.html")
def project7(request):
    return render(request,"project7.html")
def project8(request):
    return render(request,"project8.html")
def project9(request):
    return render(request,"project9.html")

def login(request):
    return render(request,'login_form.html')

def login_check(request):

    if request.method =="POST":
        user = request.POST["user"]
        print(user)
    return render(request,'index.html')