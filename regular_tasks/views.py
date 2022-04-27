from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from flock_management.models import Flocks, Coops
from .models import EggCollection, Feeds, Disinfectants, FeedingTime
from .forms import EggCollectionForm, FeedsForm, FeedingTimeForm, CoopCleaningForm
from json import dumps
from django.core import serializers
import json


def get_trays_quantity(request):
    """Get Qty of eggs per tray from db"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    trays_quantity = farmprofile[0].trays_quantity
    return JsonResponse({"trays_quantity": trays_quantity}, safe=False)


@login_required
def egg_collection(request):
    """view to current flock"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        form = EggCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form.cleaned_data = ", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value
            print(form.farm_profile)
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
        template = 'regular_tasks/egg_collection.html'
        context = {'form': form,
                   'flocks': flock}
        return render(request, template, context)


def get_feeds(request):
    """view to current flock"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    feeds = Feeds.objects.filter(farm_profile__id=farmprofile[0].id).values('feed_name')
    # feeds = Feeds.objects.values('feed_type')
    print("feeds = ", feeds)
    return JsonResponse({"feeds": list(feeds)}, safe=False)


@login_required
def feeding_time(request):
    """view to add food & water"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        form = FeedingTimeForm(request.POST)
        print(("form = ", form))
        if form.is_valid():
            print(("form.cleaned_data = ", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form
            form.farm_profile = farmprofile[0]  # Add the farmprofile ForeignKey
            previous_feeding_time = FeedingTime.objects.filter(farm_profile=farmprofile[0]).filter(flock=form.flock.id).filter(feed_name=form.feed_name).last()
            if not previous_feeding_time:
                form.feeder_amount = form.amount_food_added
                form.water_total = form.amount_water_added
            else:
                form.amount_food_consumed = previous_feeding_time.feeder_amount - form.amount_food_rem
                form.feeder_amount = previous_feeding_time.feeder_amount - form.amount_food_consumed + form.amount_food_added
            if not previous_feeding_time:
                form.water_total = form.amount_water_added
            else:
                form.amount_water_consumed = previous_feeding_time.water_total - form.amount_water_rem
                form.water_total = previous_feeding_time.water_total - form.amount_water_consumed + form.amount_water_added
            print("feeder_amount = ", form.feeder_amount)
            feed = Feeds.objects.filter(farm_profile__id=farmprofile[0].id).filter(feed_name=form.feed_name) # Get the feed object using the feed_type id submitted with the form.
            if feed:
                print("YES")
                print("feed =", feed)
                print("feed[0].qty_food = ", feed[0].qty_food)
                feed[0].qty_food -= form.amount_food_added  # Update this qty_food value by subtracting it from itself
                if feed[0].qty_food < 0:
                    feed[0].qty_food = 0
                feed[0].save()  # Save this new value to the db.
            else:
                print("NO")
                feed = Feeds(
                    farm_profile=farmprofile[0],
                    feed_name=form.feed_name,
                    qty_food=0
                )
                feed.save()
            form.save()  # Save the form fully to the db
            # Now update the qty_food value in the Feed table (will be using django signals for this at a later stage)   
            return HttpResponseRedirect('/profile')
    else:
        form = FeedingTimeForm
        flock = farmprofile[0].flocks.all()  # We can use this syntax because this model FK has a related_name provided.
        feeds = Feeds.objects.filter(farm_profile__id=farmprofile[0].id)  # This is the syntax used when the FK related_name is not provided with the model.
        template = 'regular_tasks/feeding_time.html'
        context = {'form': form,
                   'flocks': flock}
        return render(request, template, context)


def get_disinfectants(request):
    """view to current flock"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    disinfectants = Disinfectants.objects.filter(farm_profile__id=farmprofile[0].id).values('disinfectant_name')
    # feeds = Feeds.objects.values('feed_type')
    print("disinfectants = ", disinfectants)
    return JsonResponse({"disinfectants": list(disinfectants)}, safe=False)


# @login_required
def coop_cleaning(request):
    """view for Coop Cleaning"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        form = CoopCleaningForm(request.POST)
        if form.is_valid():
            print(("form.cleaned_data = ", form.cleaned_data))
            form = form.save(commit=False)
            # print(("form.disinfectant_name = ", form.disinfectant_name))
            form.farm_profile = farmprofile[0]
            disinfectant = Disinfectants.objects.filter(farm_profile__id=farmprofile[0].id).filter(disinfectant_name=form.disinfectant_name)  # Get the feed object using the feed_type id submitted with the form.
            if disinfectant:
                print("YES")
                print("disinfectant =", disinfectant)
                print("disinfectant[0].disinfectant_name = ", disinfectant[0].disinfectant_name)
            else:
                print("NO")
                disinfectant = Disinfectants(
                    farm_profile=farmprofile[0],
                    disinfectant_name=form.disinfectant_name
                )
                disinfectant.save()
            form.save()
            return HttpResponseRedirect('/profile')
    else:
        form = CoopCleaningForm
        coops = Coops.objects.filter(farm_profile__id=farmprofile[0].id)
        # disinfectants = Disinfectants.objects.all()
        template = 'regular_tasks/coop_cleaning.html'
        context = {'form': form,
                   'coops': coops}
        return render(request, template, context)
