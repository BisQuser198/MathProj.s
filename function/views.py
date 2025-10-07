from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def function_view(request, user_input):
    # a = 1
    # b = 1
    # c = 1
    # user_input = int(user_input)
    # function_hard_coded = a*user_input^2+b*user_input+c
    user_input = user_input
    user_input2 = request.GET.get('user_input')
    # value_of_F = a*user_input2^2+b*user_input2+c
    context = {'user_input1':user_input, 'user_input2':user_input2} # 'value_of_F':value_of_F
    return render(request, 'function.html', context)