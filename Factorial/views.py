from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# this works w/o a template.html
def factorial_view(request, n):
    n = int(n) 
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return HttpResponse(f"{n}! = {factorial}")

# this works w/ a template.html BUT requires import render
def factorial_template_view(request, n):
    context = {'n':n}
    return render(request, 'factorial.html', context) 