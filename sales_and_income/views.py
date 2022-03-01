from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from .forms import RoadsideSalesForm


@login_required
def sales_and_income(request):
    template = 'sales_and_income/sales_and_income.html'
    context = {}
    return render(request, template, context)


@login_required
def delivery_sales(request):
    template = 'sales_and_income/delivery_sales.html'
    context = {}
    return render(request, template, context)


@login_required
def collection_sales(request):
    template = 'sales_and_income/collection_sales.html'
    context = {}
    return render(request, template, context)


@login_required
def roadside_sales(request):
    """view to roadside sales"""
    if request.POST:
        date = request.POST['date']
        single_egg_price = request.POST['single_egg_price']
        half_dozen_eggs_price = request.POST['half_dozen_eggs_price']
        ten_eggs_price = request.POST['ten_eggs_price']
        dozen_eggs_price = request.POST['dozen_eggs_price']
        trays_of_eggs_price = request.POST['trays_of_ eggs_price']
        qty_single_eggs_remaining = request.POST['qty_single_eggs_remaining']
        qty_single_eggs_added = request.POST['qty_single_eggs_added']
        qty_half_dozen_egg_boxes_remaining = request.POST['qty_half_dozen_egg_boxes_remaining']
        qty_half_dozen_egg_boxes_added = request.POST['qty_half_dozen_egg_boxes_added']
        qty_ten_egg_boxes_remaining = request.POST['qty_ten_egg_boxes_remaining']
        qty_ten_egg_boxes_added = request.POST['qty_ten_egg_boxes_added']
        qty_dozen_egg_boxes_remaining = request.POST['qty_dozen_egg_boxes_remaining']
        qty_dozen_egg_boxes_added = request.POST['qty_dozen_egg_boxes_added']
        qty_trays_of_eggs_remaining = request.POST['qty_trays_of_eggs_remaining']
        qty_trays_of_eggs_added = request.POST['qty_trays_of_eggs_added']
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/roadside_sales.html'
    else:
        form = RoadsideSalesForm
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/roadside_sales.html'
        context = {'form': form}
        return render(request, template, context)


@login_required
def market_sales(request):
    template = 'sales_and_income/market_sales.html'
    context = {}
    return render(request, template, context)


@login_required
def bird_sales(request):
    template = 'sales_and_income/bird_sales.html'
    context = {}
    return render(request, template, context)


@login_required
def customers(request):
    template = 'sales_and_income/customers.html'
    context = {}
    return render(request, template, context)
