from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from django.http import JsonResponse
from profiles.models import UserProfile


@login_required
def flocks(request):
    """view to current flock"""
    template = 'flock_management/flocks.html'
    context = {}
    return render(request, template, context)


@login_required
def add_flock(request):
    """view to add flock"""
    template = 'flock_management/add_flock.html'
    context = {}
    return render(request, template, context)


@login_required
def bird_removal(request):
    """view to add flock"""
    template = 'flock_management/bird_removal.html'
    context = {}
    return render(request, template, context)


@login_required
def get_hens_quantity(request):
    """Get Qty of hens in a flock"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    flocks = farmprofile[0].flocks.all()
    hens_quantity = flocks[0].hens_qty
    return JsonResponse({"hens_quantity": hens_quantity}, safe=False)

