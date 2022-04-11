from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from .forms import SupplementsForm, SupplementsNameForm, MedicinesForm, MedicinesNameForm, VaccinesForm, VaccinesNameForm, DiseasesNameForm
from .models import MedicinesName, DiseasesName
import json


# Create your views here.
def supplements(request):
    """view to current flock"""
    template = 'health_and_welfare/supplements.html'
    context = {}
    return render(request, template, context)

def get_diseases(request):
    diseases = DiseasesName.objects.values('disease_name')
    return JsonResponse({"diseases": list(diseases)}, safe=False)

def get_medicines(request):
    medicines = MedicinesName.objects.values('medicine_name')
    return JsonResponse({"medicines": list(medicines)}, safe=False)

def medicines(request):
    """view to current flock"""
    form = MedicinesForm
    medicines_name = MedicinesName.objects.all()
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    flock = farmprofile[0].flocks.all()
    template = 'health_and_welfare/medicines.html'
    context = {'form': form,
               'medicines_name': medicines_name,
               'flocks': flock}
    return render(request, template, context)
