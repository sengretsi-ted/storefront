from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# # say "hello"
# def say_hello(request):
#     # return a simple http response
#     return HttpResponse("Hello World")

def calculate():
    x = 1
    y = 2
    return x  

# using the render function to render a template
def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name':'Ted'})


