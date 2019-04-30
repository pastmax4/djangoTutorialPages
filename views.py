
#from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse


# 30apr2019 massimo
# Create your views here.
def home_view(request,*args,**kwargs ):
    #return HttpResponse("<h1> Hello from world from massimo. </h1> ")
    return render(request,"home.html",{})

