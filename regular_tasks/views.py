from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from flock_management.models import Flocks, Coops
from .models import EggCollection, Feeds, Disinfectants
from .forms import EggCollectionForm, FeedingTimeForm, CoopCleaningForm


@login_required
def egg_collection(request):
    """view to current flock"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    trays_quantity = farmprofile[0].trays_quantity
    if request.POST:
        form = EggCollectionForm(request.POST, request.FILES)
        print("form raw = ", form)
        if form.is_valid():
            print("form is_valid = ", form.cleaned_data)
            form = form.save(commit=False)
            # print("form save false = ", form.cleaned_data)
            form.farm_profile = farmprofile[0]
            # print("form add profile = ", form.cleaned_data)
            # form.qty_total_eggs_laid = ((form.cleaned_data["qty_egg_trays"] * trays_quantity) + form.cleaned_data["qty_egg_singles"])
            form.save()
            return HttpResponseRedirect('/profile')
        # date = form['date']
        # flock = farmprofile[0].flocks.get(pk=int(form['flock']))
        # print("flock = ", flock)
        # if form['qty_egg_trays'] != '':
        #     qty_egg_trays = int(form['qty_egg_trays'])
        # else:
        #     qty_egg_trays = 0
        # if form['qty_egg_singles'] != '':
        #     qty_egg_singles = int(form['qty_egg_singles'])
        # else:
        #     qty_egg_singles = 0
        # qty_total_eggs_laid = ((farmprofile[0].trays_quantity * qty_egg_trays) + qty_egg_singles)
        # if form['qty_eggs_damaged'] != '':
        #     qty_eggs_damaged = int(form['qty_eggs_damaged'])
        # else:
        #     qty_eggs_damaged = 0
        # if form['qty_eggs_broken'] != '':
        #     qty_eggs_broken = int(form['qty_eggs_broken'])
        # else:
        #     qty_eggs_broken = 0
        # if form['qty_eggs_personal_use'] != '':
        #     qty_eggs_personal_use = int(form['qty_eggs_personal_use'])
        # else:
        #     qty_eggs_personal_use = 0
        # if form['qty_eggs_given_free'] != '':
        #     qty_eggs_given_free = int(form['qty_eggs_given_free'])
        # else:
        #     qty_eggs_given_free = 0
        # if form['weight_total_eggs_laid'] != '':
        #     weight_total_eggs_laid = int(form['weight_total_eggs_laid'])
        #     avg_egg_weight = (weight_total_eggs_laid / qty_total_eggs_laid)
        # else:
        #     weight_total_eggs_laid = 0
        #     avg_egg_weight = 0
        # egg_collection_notes = form['egg_collection_notes']
        # # image_url = request.POST['image_url']
        # task = EggCollection(
        #     farm_profile=farmprofile[0],
        #     date=date,
        #     flock=flock,
        #     qty_egg_trays=qty_egg_trays,
        #     qty_egg_singles=qty_egg_singles,
        #     qty_total_eggs_laid=qty_total_eggs_laid,
        #     qty_eggs_damaged=qty_eggs_damaged,
        #     qty_eggs_broken=qty_eggs_broken,
        #     qty_eggs_personal_use=qty_eggs_personal_use,
        #     qty_eggs_given_free=qty_eggs_given_free,
        #     weight_total_eggs_laid=weight_total_eggs_laid,
        #     avg_egg_weight=avg_egg_weight,
        #     qty_saleable_eggs=(qty_total_eggs_laid - (qty_eggs_damaged + qty_eggs_broken + qty_eggs_personal_use + qty_eggs_given_free)),
        #     egg_collection_notes=egg_collection_notes
        # )
        # task.save()
        # farm = farmprofile[0]
        # eggs_in_stock = farm.eggs_in_stock + (qty_total_eggs_laid - (qty_eggs_damaged + qty_eggs_broken + qty_eggs_personal_use + qty_eggs_given_free))
        # farm.eggs_in_stock = eggs_in_stock
        # farm.save()
        # template = 'profiles/dashboard.html'
        # return render(request, template)
    else:
        form = EggCollectionForm
        flock = farmprofile[0].flocks.all()
        print("flock = ", flock)
        template = 'regular_tasks/egg_collection.html'
        context = {'form': form,
                   'flocks': flock,
                   'trays_quantity': trays_quantity}
        return render(request, template, context)


@login_required
def feeding_time(request):
    """view to add food & water"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        form = FeedingTimeForm(request.POST)
        if form.is_valid():
            # print("form cleaned = ", form.cleaned_data)
            form = form.save(commit=False)
            form.farm_profile = farmprofile[0]
            # print("form cleaned = ", form)
            form.save()
            # print("form cleaned = ", form)
            feed = Feeds.objects.get(pk=form.feed_type.id)
            feed.qty_food -= form.amount_food_added
            feed.save()
            return HttpResponseRedirect('/profile')
    else:
        form = FeedingTimeForm
        flock = farmprofile[0].flocks.all()
        feeds = Feeds.objects.filter(farm_profile__id=farmprofile[0].id)
        template = 'regular_tasks/feeding_time.html'
        context = {'form': form,
                   'flocks': flock,
                   'feeds': feeds}
        return render(request, template, context)


@login_required
def coop_cleaning(request):
    """view for Coop Cleaning"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        form = CoopCleaningForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')
    else:
        form = CoopCleaningForm
        coops = Coops.objects.filter(farm_profile__id=farmprofile[0].id)
        disinfectants = Disinfectants.objects.all()
        template = 'regular_tasks/coop_cleaning.html'
        context = {'form': form,
                   'coops': coops,
                   'disinfectants': disinfectants}
        return render(request, template, context)
