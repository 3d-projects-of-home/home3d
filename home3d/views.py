from django.shortcuts import render
from django.http import HttpResponseRedirect
from service.models import service

def homepage(request):
    try:
        code=request.GET['name']
        if service.objects.filter(service_token=code).exists():
            service_link=service.objects.filter(service_token=code)
        else:
            service_link="Non"
        data={'service_link':service_link}
        #return HttpResponseRedirect("/home_view/",data)
        return render(request,"homeview.html",data)
    except:
        pass
    return render(request,"index.html")

def example(request):
    return render(request,"example.html")

def home(request):
    return render(request,"homeview.html")