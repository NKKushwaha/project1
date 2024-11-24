from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view1(request):
    return HttpResponse ('Hello')


def view2(request):
    return HttpResponse ('<h1>Hello</h1>')


def view3(request):
    return HttpResponse ('''<h1><marquee> move </marquee></h1>
                         <b>hay</b>
                         ''')