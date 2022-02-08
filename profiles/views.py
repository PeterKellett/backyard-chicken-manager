from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from .models import UserProfile, FarmProfile, FarmType


# Create your views here.
@login_required
def dashboard(request):
    '''Render User dashboard'''
    context = {

    }
    template = 'profiles/dashboard.html'
    return render(request, template, context)


@login_required
def onboard_personal(request):
    '''Render onboarding step 1'''
    profile = get_object_or_404(CustomUser, email=request.user)
    print("profile = ", profile)
    first_name = 'john'
    last_name = 'smith'
    userprofile = UserProfile(
        user=profile,
        first_name=first_name,
        last_name=last_name,
    )
    userprofile.save()
    context = {

    }
    template = 'profiles/onboard_personal.html'
    return render(request, template, context)


@login_required
def onboard_farm(request):
    '''Render onboarding step 2'''
    farm_types = FarmType.objects.all()
    for farm_type in farm_types:
        farm_type = str(farm_type)
        print(farm_type)
        print(type(farm_type))
 
    context = {
        "farm_types": farm_types
    }
    template = 'profiles/onboard_farm.html'
    return render(request, template, context)


@login_required
def onboard_flock(request):
    '''Render onboarding step 3'''
    context = {

    }
    template = 'profiles/onboard_flock.html'
    return render(request, template, context)


@login_required
def onboard_produce(request):
    '''Render onboarding step 4'''
    context = {

    }
    template = 'profiles/onboard_produce.html'
    return render(request, template, context)


@login_required
def onboard_stock(request):
    '''Render onboarding step 5'''
    context = {

    }
    template = 'profiles/onboard_stock.html'
    return render(request, template, context)
