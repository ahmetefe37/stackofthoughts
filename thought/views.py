from django.shortcuts import render,HttpResponse

# Create your views here.

def f_homepage(request):
    return HttpResponse("Anasayfa")