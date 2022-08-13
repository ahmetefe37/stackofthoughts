# python system modules
from django.shortcuts import render

# my modules


# --------------------------------------------------------------

# home page funct
def f_homepage(request):
    context = {}
    return render(request,"thought/homepage.html",context)


# detail page funct
def f_detailpage(request):
    context = {}
    return render(request,"thought/detailpage.html",context)


# contact page funct
def f_contactpage(request):
    context = {}
    return render(request,"thought/contactpage.html",context)


# about us page funct
def f_aboutuspage(request):
    context = {}
    return render(request,"thought/aboutuspage.html",context)


# profile page funct
def f_profilepage(request):
    context = {}
    return render(request,"thought/profilepage.html",context)


# register page funct
def f_registerpage(request):
    context = {}
    return render(request,"thought/registerpage.html",context)


# login page funct
def f_loginpage(request):
    context = {}
    return render(request,"thought/loginpage.html",context)



