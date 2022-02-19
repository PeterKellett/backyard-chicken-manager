from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser


@login_required
def egg_collection(request):
    """view to current flock"""
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
