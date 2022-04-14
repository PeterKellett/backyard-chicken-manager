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
# def get_supplements(request):
#     """view to current flock"""
#     supplements = SupplementsName.objects.values('supplement_name')
#     return JsonResponse({"supplements": list(supplements)}, safe=False)


def supplements(request):
    """view to current flock"""
    # The three lines below can be deleted once the rest of the code has 
    # been uncommented and implemented
    template = 'health_and_welfare/supplements.html'
    context = {}
    return render(request, template, context)

    # supplements_name = SupplementsName.objects.all()
    # userprofile = UserProfile.objects.get(user=request.user)
    # farmprofile = userprofile.farmprofiles.all()
    # if request.POST:
    #     form = SupplementsForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         print(("form.cleaned_data = ", form.cleaned_data))
    #         form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
    #         form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value
    #         print("form farm profile :", form.farm_profile)
    #         # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
    #         # because setting the model default = 0 affects floating labels.
    #         if not form.doseage_amount:
    #             form.doseage_amount = 0
    #         form.save()  # Save the form fully.
    #         farm = farmprofile[0]  # Refer to the farmprofile object which is obtained above
    #         farm.save()  # Save the farmprofile to the db.
    #         return HttpResponseRedirect('/health_and_welfare/supplements/')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    # else:
    #     form = SupplementsForm
    #     flock = farmprofile[0].flocks.all()
    #     print("flock = ", flock)
    #     template = 'health_and_welfare/supplements.html'
    #     context = {'form': form,
    #                'supplement_name': supplement_name,
    #                'flocks': flock}
    #     print("context :", type(context))
    #     return render(request, template, context)


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
    medicines_name = MedicinesName.objects.all()
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
            if not form.doseage_amount:
                form.doseage_amount = 0
            form.save()  # Save the form fully.
            farm = farmprofile[0]  # Refer to the farmprofile object which is obtained above
            farm.save()  # Save the farmprofile to the db.
            return HttpResponseRedirect('/health_and_welfare/medicines/')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = MedicinesForm
        flock = farmprofile[0].flocks.all()
        print("flock = ", flock)
        template = 'health_and_welfare/medicines.html'
        context = {'form': form,
                   'medicines_name': medicines_name,
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
    vaccines_name = VaccinesName.objects.all()
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        form = VaccinesForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form.cleaned_data = ", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value
            print("form farm profile :", form.farm_profile)
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not form.doseage_amount:
                form.doseage_amount = 0
            form.save()  # Save the form fully.
            farm = farmprofile[0]  # Refer to the farmprofile object which is obtained above
            farm.save()  # Save the farmprofile to the db.
            return HttpResponseRedirect('/health_and_welfare/vaccines/')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = VaccinesForm
        flock = farmprofile[0].flocks.all()
        print("flock = ", flock)
        template = 'health_and_welfare/vaccines.html'
        context = {'form': form,
                   'vaccines_name': vaccines_name,
                   'flocks': flock}
        print("context :", type(context))
        return render(request, template, context)
