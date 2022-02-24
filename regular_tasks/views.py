from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from flock_management.models import Flocks


@login_required
def egg_collection(request):
    """view to current flock"""
    if request.POST:
        print("String")
        date = request.POST['date']
        flockName = request.POST['date']
        qtyTray = request.POST['date']
        qtySingle = request.POST['date']
        qtyTotal = request.POST['date']
        qtyDamaged = request.POST['date']
        qtyBroken = request.POST['date']
        qtyPersonal = request.POST['date']
        qtyFree = request.POST['date']
        weightLaid = request.POST['date']
        weightIndividual = request.POST['date']
        weightAverage = request.POST['date']
        qtySaleable = request.POST['date']
        print("Date: ", date)
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        print("FarmpPofile.id: ", farmprofile)
        #flocks = userprofile.farmprofiles.flocks.all()
        #print(flocks)
        #context = {
        #    'flocks': flocks
        #}
        template = 'profiles/dashboard.html'
        return render(request, template)
    else: 
        template = 'regular_tasks/egg_collection.html'
        context = {}
        return render(request, template, context)

@login_required
def feeding_time(request):
    """view to add flock"""
    template = 'regular_tasks/feeding_time.html'
    context = {}
    return render(request, template, context)

@login_required
def coop_cleaning(request):
    """view to add flock"""
    template = 'regular_tasks/coop_cleaning.html'
    context = {}
    return render(request, template, context)
