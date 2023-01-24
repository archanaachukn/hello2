
from django.shortcuts import render
from .models import place, name

def demo(request):
    obj=place.objects.all()
    obj1=name.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})