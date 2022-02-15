from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser


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
