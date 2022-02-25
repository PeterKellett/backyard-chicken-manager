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
        flock = request.POST['flock_name']
        qty_total_trays = request.POST['qty-trays']
        qty_total_single = request.POST['qty-singles']
        qty_total_laid = request.POST['total_eggs_laid']
        qty_damaged = request.POST['eggs_damaged']
        qty_broken = request.POST['eggs_broken']
        qty_personal_use = request.POST['eggs_personal_use']
        qty_given_free = request.POST['eggs_given_free']
        weight_total_laid = request.POST['total_weight']
        avg_egg_weight = request.POST['average_egg_weight']
        qty_saleable = request.POST['eggs_saleable_qty']
        egg_collection_notes = request.POST['notes']
        image_url = request.POST['image_url']
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
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
