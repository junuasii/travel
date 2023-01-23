from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Member

# Create your views here.
def index(request):
    obj=Place.objects.all()
    mem=Member.objects.all()
    return render(request,"index.html",{'result':obj,'clct':mem})

# def calculate(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x//y
#     return render(request,"result.html",{'addt':add,'subt':sub,'mult':mul,'divs':div})
#
#
