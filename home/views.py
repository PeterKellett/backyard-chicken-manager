from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    '''A view to return the homepage'''  
    return redirect('account_signup')
    # return render(request, template, context)
