from django.shortcuts import render


# Create your views here.
def health_and_wellfare(request):
    """view to current flock"""
    template = 'profiles/dashboard.html'
    context = {}
    return render(request, template, context)
