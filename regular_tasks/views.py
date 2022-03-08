from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from flock_management.models import Flocks
from .models import EggCollection
from .forms import EggCollectionForm, FeedingTimeForm, CoopCleaningForm


@login_required
def egg_collection(request):
    """view to current flock"""
    userprofile = UserProfile.objects.get(user=request.user)
    print("userprofile = ", userprofile)
    farmprofile = userprofile.farmprofiles.all()
    print("farmprofile = ", farmprofile)
    print("qty eggs in stock = ", farmprofile[0].eggs_in_stock)
    if request.POST:
        form = request.POST
        print("form = ", form)
        date = form['date']
        # flock = int(request.POST['flock'])
        flock = farmprofile[0].flocks.get(pk=int(form['flock']))
        print("flock = ", flock)
        if form['qty_egg_trays'] != '':
            qty_egg_trays = int(form['qty_egg_trays'])
        else:
            qty_egg_trays = 0
        if form['qty_egg_singles'] != '':
            qty_egg_singles = int(form['qty_egg_singles'])
        else:
            qty_egg_singles = 0
        qty_total_eggs_laid = ((farmprofile[0].trays_quantity * qty_egg_trays) + qty_egg_singles)
        if form['qty_eggs_damaged'] != '':
            qty_eggs_damaged = int(form['qty_eggs_damaged'])
        else:
            qty_eggs_damaged = 0
        if form['qty_eggs_broken'] != '':
            qty_eggs_broken = int(form['qty_eggs_broken'])
        else:
            qty_eggs_broken = 0
        if form['qty_eggs_personal_use'] != '':
            qty_eggs_personal_use = int(form['qty_eggs_personal_use'])
        else:
            qty_eggs_personal_use = 0
        if form['qty_eggs_given_free'] != '':
            qty_eggs_given_free = int(form['qty_eggs_given_free'])
        else:
            qty_eggs_given_free = 0
        if form['weight_total_eggs_laid'] != '':
            weight_total_eggs_laid = int(form['weight_total_eggs_laid'])
            avg_egg_weight = (weight_total_eggs_laid / qty_total_eggs_laid)
        else:
            weight_total_eggs_laid = 0
            avg_egg_weight = 0
        egg_collection_notes = form['egg_collection_notes']
        # image_url = request.POST['image_url']
        task = EggCollection(
            farm_profile=farmprofile[0],
            date=date,
            flock=flock,
            qty_egg_trays=qty_egg_trays,
            qty_egg_singles=qty_egg_singles,
            qty_total_eggs_laid=qty_total_eggs_laid,
            qty_eggs_damaged=qty_eggs_damaged,
            qty_eggs_broken=qty_eggs_broken,
            qty_eggs_personal_use=qty_eggs_personal_use,
            qty_eggs_given_free=qty_eggs_given_free,
            weight_total_eggs_laid=weight_total_eggs_laid,
            avg_egg_weight=avg_egg_weight,
            qty_saleable_eggs=(qty_total_eggs_laid - (qty_eggs_damaged + qty_eggs_broken + qty_eggs_personal_use + qty_eggs_given_free)),
            egg_collection_notes=egg_collection_notes
        )
        task.save()
        farm = farmprofile[0]
        eggs_in_stock = farm.eggs_in_stock + (qty_total_eggs_laid - (qty_eggs_damaged + qty_eggs_broken + qty_eggs_personal_use + qty_eggs_given_free))
        print("eggs_in_stock = ", eggs_in_stock)
        farm.eggs_in_stock = eggs_in_stock
        farm.save()
        template = 'profiles/dashboard.html'
        return render(request, template)
    else:
        form = EggCollectionForm
        flock = farmprofile[0].flocks.all()
        print("flock = ", flock)
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
