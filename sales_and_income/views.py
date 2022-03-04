from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from .forms import EggRoadsideSalesForm, EggCollectionSalesForm, EggDeliverySalesDashboardForm, EggDeliverySalesForm, EggMarketSalesForm


@login_required
def sales_and_income(request):
    """sales & Income View"""
    template = 'sales_and_income/sales_and_income.html'
    context = {}
    return render(request, template, context)


@login_required
def egg_delivery_sales_dashboard(request):
    """egg delivery sales dashboard view"""
    if request.POST:
        date = request.POST['date']
        breakages_and_loses_eggs_delivery = request.POST['breakages_and_loses_eggs_delivery']
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/egg_delivery_sales_dashboard.html'
    else:
        form = EggDeliverySalesForm
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/egg_delivery_sales_dashboard.html'
        context = {'form': form}
        return render(request, template, context)


@login_required
def egg_delivery_sales(request):
    if request.POST:
        date = request.POST['date']
        customer_name_eggs_delivery = request.POST['customer_name_eggs_delivery']
        normal_order_qty_eggs_delivery = request.POST['normal_order_qty_eggs_delivery']
        delivery_due_date = request.POST['delivery_due_date']
        delivery_not_made = request.POST['delivery_not_made']
        delivery_not_made_reason = request.POST['delivery_not_made_reason']
        qty_sold_eggs_delivery = request.POST['qty_sold_eggs_delivery']
        qty_given_free_eggs_delivery = request.POST['qty_given_free_eggs_delivery']
        amount_paid_eggs_delivery = request.POST['amount_paid_eggs_delivery']
        balance_owed_eggs_delivery = request.POST['balance_owed_eggs_delivery']
        breakages_and_loses_eggs_delivery = request.POST['breakages_and_loses_eggs_delivery']
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/egg_delivery_sales.html'
    else:
        form = EggDeliverySalesForm
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/egg_delivery_sales.html'
        context = {'form': form}
        return render(request, template, context)


@login_required
def egg_collection_sales(request):
    if request.POST:
        date = request.POST['date']
        customer_name_eggs_collection = request.POST['customer_name_eggs_collection']
        normal_order_qty_eggs_collection = request.POST['normal_order_qty_eggs_collection']
        qty_sold_eggs_collection = request.POST['qty_sold_eggs_collection']
        qty_given_free_eggs_collection = request.POST['qty_given_free_eggs_collection']
        amount_paid_eggs_collection = request.POST['amount_paid_eggs_collection']
        balance_owed_eggs_collection = request.POST['balance_owed_eggs_collection']
        breakages_and_loses_eggs_collection = request.POST['breakages_and_loses_eggs_collection']
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/egg_collection_sales.html'
    else:
        form = EggCollectionSalesForm
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/egg_collection_sales.html'
        context = {'form': form}
        return render(request, template, context)


@login_required
def egg_roadside_sales(request):
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
        amount_paid_eggs_roadside = request.POST['amount_paid_eggs_roadside']
        sales_amount_eggs_roadside = request.POST['sales_amount_eggs_roadside']
        sales_paid_difference_eggs_roadside = request.POST['sales_paid_difference_eggs_roadside']
        loses_eggs_roadside = request.POST['loses_eggs_roadside']
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/egg_roadside_sales.html'
    else:
        form = EggRoadsideSalesForm
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/egg_roadside_sales.html'
        context = {'form': form}
        return render(request, template, context)


@login_required
def egg_market_sales(request):
    """view to market sales"""
    if request.POST:
        date = request.POST['date']
        venue_location_eggs_market = request.POST['venue_location_eggs_market']
        single_egg_price = request.POST['single_egg_price']
        half_dozen_eggs_price = request.POST['half_dozen_eggs_price']
        ten_eggs_price = request.POST['ten_eggs_price']
        dozen_eggs_price = request.POST['dozen_eggs_price']
        trays_of_eggs_price = request.POST['trays_of_ eggs_price']
        qty_single_eggs_sold = request.POST['qty_single_eggs_sold']
        qty_half_dozen_egg_boxes_sold = request.POST['qty_half_dozen_egg_boxes_sold']
        qty_ten_egg_boxes_sold = request.POST['qty_ten_egg_boxes_sold']
        qty_dozen_egg_boxes_sold = request.POST['qty_dozen_egg_boxes_sold']
        qty_trays_of_eggs_sold = request.POST['qty_trays_of_eggs_sold']
        amount_paid_eggs_market = request.POST['amount_paid_eggs_market']
        sales_amount_eggs_roadside = request.POST['sales_amount_eggs_roadside']
        sales_paid_difference_eggs_roadside = request.POST['sales_paid_difference_eggs_roadside']
        loses_eggs_market = request.POST['loses_eggs_market']
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/egg_market_sales.html'
    else:
        form = EggMarketSalesForm
        userprofile = UserProfile.objects.get(user=request.user)
        farmprofile = userprofile.farmprofiles.all()
        template = 'sales_and_income/egg_market_sales.html'
        context = {'form': form}
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
