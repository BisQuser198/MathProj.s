from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def function_view(request):
#    a, b, c = 1, 1, 1

    print(request.GET) # this is a dictionary
    user_input = request.GET.get('user_input') # return user_input
    user_input2 = request.GET.get('user_input2')
    user_input3 = request.GET.get('user_input3')
    print(user_input) ; print(user_input2)

    # Retrieve previous value_of_F from session
    previous_value_of_F = request.session.get('value_of_F')


# save user_input for processing
    context = {'user_input': user_input, 
               'user_input2': user_input2,
                'user_input3': user_input3,
                'previous_value_of_F': previous_value_of_F,
                'value_of_F': None,
               } 
# prevent errors if user_input is None or not numeric
    try:
#        if user_input.isnumeric():
#        if user_input.isnumeric() and user_input2.isnumeric() and user_input3.isnumeric():
#        if all(val and val.isnumeric() for val in [user_input, user_input2, user_input3]):
            x, a, b = int(user_input), int(user_input2), int(user_input3)
            value_of_F = a* (x**2) + b*x
            print(value_of_F)
            context['value_of_F'] = value_of_F
 #   except:
 #       pass
             # Save current value_of_F to session for next interaction
            request.session['value_of_F'] = value_of_F
    
    except Exception as e:
        print(e)
        pass
    return render(request, 'function.html', context)