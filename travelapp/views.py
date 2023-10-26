from django.http import HttpResponse
from django.shortcuts import render
from.models import place,member
# Create your views here.
def demo(request):
    # return HttpResponse("helloworld")
    # name = "india"
    # return render(request,"home.html",{'obj':name})
    obj=place.objects.all()
    objj=member.objects.all()
    return render(request,"index.html",{'result':obj,'results':objj})
# def about(request):
#     return render(request, "about.html")
# def contact(request):
#     return HttpResponse("hello am contct")
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})