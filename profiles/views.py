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
    context = {

    }
    template = 'profiles/onboard_personal.html'
    return render(request, template, context)


@login_required
def onboard_farm(request):
    '''Render onboarding step 2'''
    farm_types = FarmType.objects.all()
    print(farm_types)
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
