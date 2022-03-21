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
        form = EggCollectionForm(request.POST)
        if form.is_valid():
            print(("form cleaned date =", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not form.qty_egg_trays:
                form.qty_egg_trays = 0
            if not form.qty_egg_singles:
                form.qty_egg_singles = 0
            if not form.qty_eggs_damaged:
                form.qty_eggs_damaged = 0
            if not form.qty_eggs_broken:
                form.qty_eggs_broken = 0
            if not form.qty_eggs_personal_use:
                form.qty_eggs_personal_use = form.qty_eggs_damaged  # This is a customised value to allow for damaged eggs to be used for personal eggs in egg calculations below.
            if not form.qty_eggs_given_free:
                form.qty_eggs_given_free = 0
            if not form.weight_total_eggs_laid:
                form.weight_total_eggs_laid = 0
            # Form update and calculations for qty_total_eggs_laid, qty_saleable_eggs, avg_egg_weight fields
            form.qty_total_eggs_laid = ((farmprofile[0].trays_quantity * form.qty_egg_trays) + form.qty_egg_singles)
            form.qty_saleable_eggs = form.qty_total_eggs_laid - (form.qty_eggs_damaged + (form.qty_eggs_personal_use - form.qty_eggs_damaged) + form.qty_eggs_broken + form.qty_eggs_given_free)
            form.avg_egg_weight = (form.weight_total_eggs_laid / form.qty_total_eggs_laid)
            form.save()  # Save the form fully.
            # Update 'eggs_in_stock' field of the FarmProfile of the user (signals)
            farm = farmprofile[0]  # Refer to the farmprofile object which is obtained above
            farm.eggs_in_stock += form.qty_saleable_eggs  # Update the eggs_in_stock value to itself
            farm.save()  # Save the farmprofile to the db.
            return HttpResponseRedirect('/profile')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
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
            form = form.save(commit=False)  # Presave the form
            form.farm_profile = farmprofile[0]  # Add the farmprofile ForeignKey
            form.save()  # Save the form fully to the db
            # Now update the qty_food value in the Feed table (will be using django signals for this at a later stage)
            feed = Feeds.objects.get(pk=form.feed_type.id)  # Get the feed object using the feed_type id submitted with the form.
            feed.qty_food -= form.amount_food_added  # Update this qty_food value by subtracting it from itself
            feed.save()  # Save this new value to the db.
            return HttpResponseRedirect('/profile')
    else:
        form = FeedingTimeForm
        flock = farmprofile[0].flocks.all()  # We can use this syntax because this model FK has a related_name provided.
        feeds = Feeds.objects.filter(farm_profile__id=farmprofile[0].id)  # This is the syntax used when the FK related_name is not provided with the model.
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
