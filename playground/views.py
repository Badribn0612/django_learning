from django.shortcuts import render
from django.http import HttpResponse

# # Create your views here.
# def say_hello(request):
#     # In realworld we can pull data from database
#     # We can transform data
#     return HttpResponse("Hello, World!") # Now we have to map this view to a URL. When we have a request to that URL
#             # this view will be called. 

def calculate():
    x = 1
    y = 2
    return x + y

def say_hello(request):
    x = calculate()
    return render(request, "hello.html", {"name": x})
 