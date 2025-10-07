from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def function_view(request):
    a, b, c = 1, 2, 1

    print(request.GET) # this is a dictionary
    user_input = request.GET.get('user_input') # return user_input
    user_input2 = request.GET.get('user_input2')
    print(user_input) ; print(user_input2)
    
    context = {'user_input': user_input, 
               'user_input2': user_input2,
               } # save user_input for processing
    
    try:
        if user_input.isnumeric():
            value_of_F = (int(user_input)**2) #+ b*int(user_input) + c
            context['value_of_F'] = value_of_F
            print(value_of_F)
    except:
        pass
    return render(request, 'function.html', context)