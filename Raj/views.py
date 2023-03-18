from django.shortcuts import render

# Create your views here.

def Dhoni(request):
    return render(request,'Dhoni.html')

def Virat(request):
    return render(request,'Virat.html')

def Abd(request):
    return render(request,'Abd.html')