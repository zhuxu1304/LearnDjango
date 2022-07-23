from django.shortcuts import render
from django.http import HttpResponse
from .models import It, ToDoList


# Create your views here.
def showSomeThing(response):
    return HttpResponse("This is the homepage")


def showAnother(response):
    return HttpResponse('this is something else')


def showToDoList(response, name):
    ls = ToDoList.objects.get(name=name)
    first = ls.it_set.get(id=1)
    second = ls.it_set.get(id=2)
    return HttpResponse('<h1>%s</h1><br></br><p>%s</p><br></br><p>%s</p>' % (str(ls), str(first), str(second)))
