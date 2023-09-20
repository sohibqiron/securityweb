from django.shortcuts import render
from .models import Security

# Create your views here.

def test(request):
    return render(request,'mainapp/test.html')


def index(request):
    return render(request,'mainapp/index.html')


def service(request):
    return render(request,'mainapp/service.html')


def guard(request):
    securitys = Security.objects.all()
    
    context = {
        "securitys":securitys
    }
    return render(request,'mainapp/guard.html',context)
