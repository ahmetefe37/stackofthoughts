from django.shortcuts import render

# Create your views here.

def f_homepage(request):
    context = {}
    return render(request,"thought/homepage.html",context)