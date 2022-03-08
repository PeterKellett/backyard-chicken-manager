from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from flock_management.models import Flocks
from .forms import EggCollectionForm, FeedingTimeForm, CoopCleaningForm


@login_required
def egg_collection(request):
    """view to current flock"""
    if request.POST:
        date = request.POST['date']
        flock = request.POST['flock_name']
        qty_egg_trays = request.POST['qty_egg_trays']
        qty_egg_singles = request.POST['qty_egg_singles']
        qty_total_eggs_laid = request.POST['qty_total_eggs_laid']
        qty_eggs_damaged = request.POST['qty_eggs_damaged']
        qty_eggs_broken = request.POST['qty_eggs_broken']
        qty_eggs_personal_use = request.POST['qty_eggs_personal_use']
        qty_eggs_given_free = request.POST['qty_eggs_given_free']
        weight_total_eggs_laid = request.POST['weight_total_eggs_laid']
        avg_egg_weight = request.POST['avg_egg_weight']
        qty_saleable_eggs = request.POST['qty_saleable_eggs']
        egg_collection_notes = request.POST['egg_collection_notes']
        # image_url = request.POST['image_url']
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'profiles/dashboard.html'
        return render(request, template)
    else:
        form = EggCollectionForm
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        flock = farmprofile[0].flocks.all()
        template = 'regular_tasks/egg_collection.html'
        context = {'form': form,
                   'flocks': flock}
        return render(request, template, context)


@login_required
def feeding_time(request):
    """view to add food & water"""
    form = FeedingTimeForm
    if request.POST:
        date = request.POST['date']
        flock = request.POST['flock_name']
        food_type = request.POST['food_type']
        amount_food_rem = request.POST['amount_food_rem']
        amount_food_added = request.POST['amount_food_added']
        amount_water_rem = request.POST['amount_water_rem']
        amount_water_added = request.POST['amount_water_added']
        feeding_notes = request.POST['feeding_notes']
        template = 'profiles/dashboard.html'
        context = {}
        return render(request, template)
    else:
        template = 'regular_tasks/feeding_time.html'
        context = {'form': form}
        return render(request, template, context)


@login_required
def coop_cleaning(request):
    """view for Coop Cleaning"""
    form = CoopCleaningForm
    if request.POST:
        date = request.POST['date']
        flock = request.POST['flock_name']
        disinfected = request.POST['disinfected']
        disinfectant = request.POST['disinfectant']
        coop_cleaning_notes = request.POST['coop_cleaning_notes']
        template = 'profiles/dashboard.html'
        context = {}
        return render(request, template)
    else:
        template = 'regular_tasks/coop_cleaning.html'
        context = {'form': form}
        return render(request, template, context)
