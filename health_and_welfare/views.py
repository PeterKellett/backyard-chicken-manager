from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from .forms import SupplementsForm, SupplementsNameForm, MedicinesForm, MedicinesNameForm, VaccinesForm, VaccinesNameForm
from .models import MedicinesName, DiseasesName, VaccinesName, VirusesName, SupplementsName
import json


# Create your views here.
def get_supplements(request):
    """view to current supplements"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    supplements = SupplementsName.objects.filter(farm_profile__id=farmprofile[0].id).values('supplement_name')
    print("supplements = ", supplements)
    return JsonResponse({"supplements": list(supplements)}, safe=False)


def supplements(request):
    """view to supplements"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        print("POST")
        form = SupplementsForm(request.POST)
        print(("form = ", form))
        if form.is_valid():
            print(("form.cleaned_data = ", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form
            form.farm_profile = farmprofile[0]  # Add the farmprofile ForeignKey
            if not form.qty_hens:
                form.qty_hens = 0
            if not form.qty_chicks:
                form.qty_chicks = 0
            if not form.qty_cocks:
                form.qty_cocks = 0
            form.dose_per_bird = (form.dosage_amount / (form.qty_hens + form.qty_chicks + form.qty_cocks))
            supplement = SupplementsName.objects.filter(farm_profile__id=farmprofile[0].id).filter(supplement_name=form.supplement_name)  # Get the supplement object using the supplement_name submitted with the form.
            if supplement:
                print("YES SUPPLEMENT")
                supplement[0].supplement_in_stock -= form.dosage_amount  # Update this qty_food value by subtracting it from itself
                if supplement[0].supplement_in_stock < 0:
                    supplement[0].supplement_in_stock = 0
                supplement[0].save()  # Save this new value to the db.
            else:
                print("NO SUPPLEMENT")
                supplement = SupplementsName(
                    farm_profile=farmprofile[0],
                    supplement_name=form.supplement_name,
                    supplement_in_stock=0
                )
                supplement.save()
            form.save()
            return HttpResponseRedirect('/profile')
        else:
            print("NOT VALID")
            print(("form = ", form.cleaned_data))
    else:
        form = SupplementsForm
        flock = farmprofile[0].flocks.all()
        print("flock = ", flock)
        template = 'health_and_welfare/supplements.html'
        context = {'form': form,
                   'flocks': flock}
        return render(request, template, context)


def get_diseases(request):
    """view to current flock"""
    diseases = DiseasesName.objects.values('disease_name')
    return JsonResponse({"diseases": list(diseases)}, safe=False)


def get_medicines(request):
    """view to current flock"""
    medicines = MedicinesName.objects.values('medicine_name')
    return JsonResponse({"medicines": list(medicines)}, safe=False)


def medicines(request):
    """view to current flock"""
    # medicines_name = MedicinesName.objects.all()
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        form = MedicinesForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form.cleaned_data = ", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value
            print("form farm profile :", form.farm_profile)
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not form.qty_hens:
                form.qty_hens = 0
            if not form.qty_chicks:
                form.qty_chicks = 0
            if not form.qty_cocks:
                form.qty_cocks = 0
            form.dose_per_bird = (form.dosage_amount / (form.qty_hens + form.qty_chicks + form.qty_cocks))
            medicine = MedicinesName.objects.filter(farm_profile__id=farmprofile[0].id).filter(medicine_name=form.medicine_name)  # Get the feed object using the feed_type id submitted with the form.
            if not medicine:
                print("YES")
                medicine_name = MedicinesName(
                    farm_profile=farmprofile[0],
                    medicine_name=form.medicine_name
                )
                medicine_name.save()
            form.save()  # Save the form fully.
            return HttpResponseRedirect('/health_and_welfare/medicines/')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = MedicinesForm
        flock = farmprofile[0].flocks.all()
        print("flock = ", flock)
        template = 'health_and_welfare/medicines.html'
        context = {'form': form,
                   'flocks': flock}
        print("context :", type(context))
        return render(request, template, context)


def get_viruses(request):
    viruses = VirusesName.objects.values('virus_name')
    return JsonResponse({"viruses": list(viruses)}, safe=False)


def get_vaccines(request):
    vaccines = VaccinesName.objects.values('vaccine_name')
    return JsonResponse({"vaccines": list(vaccines)}, safe=False)


def vaccines(request):
    """view to current flock"""
    # vaccines_name = VaccinesName.objects.all()
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        form = VaccinesForm(request.POST, request.FILES)
        print("form = ", form)
        if form.is_valid():
            print(("form.cleaned_data = ", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value
            print("form farm profile :", form.farm_profile)
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not form.qty_hens:
                form.qty_hens = 0
            if not form.qty_chicks:
                form.qty_chicks = 0
            if not form.qty_cocks:
                form.qty_cocks = 0
            form.dose_per_bird = (form.dosage_amount / (form.qty_hens + form.qty_chicks + form.qty_cocks))
            vaccine = VaccinesName.objects.filter(farm_profile__id=farmprofile[0].id).filter(vaccine_name=form.vaccine_name)
            form.save()  # Save the form fully.
            return HttpResponseRedirect('/health_and_welfare/vaccines/')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
        else:
            print("NOT VALID")
    else:
        form = VaccinesForm
        flock = farmprofile[0].flocks.all()
        # print("flock = ", flock)
        template = 'health_and_welfare/vaccines.html'
        context = {'form': form,
                   'flocks': flock}
        print("context :", type(context))
        return render(request, template, context)
