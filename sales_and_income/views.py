from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from .forms import EggRoadsideSalesForm, EggCollectionSalesForm, EggDeliverySalesDashboardForm, EggDeliverySalesForm, EggMarketSalesForm # EggCollectionSalesDashboardForm 


@login_required
def sales_and_income(request):
    """sales & Income View"""
    template = 'sales_and_income/sales_and_income.html'
    context = {}
    return render(request, template, context)


@login_required
def egg_roadside_sales(request):
    """view to roadside sales"""
    # userprofile = UserProfile.objects.get(user=request.user)
    # farmprofile = userprofile.farmprofiles.all()
    # print(farmprofile)
    if request.POST:
        form = EggRoadsideSalesForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form cleaned date =", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not form.single_egg_price:
                form.single_egg_price = 0
            if not form.half_dozen_eggs_price:
                form.half_dozen_eggs_price = 0
            if not form.ten_eggs_price:
                form.ten_eggs_price = 0
            if not form.dozen_eggs_price:
                form.dozen_eggs_price = 0
            if not form.trays_of_eggs_price:
                form.trays_of_eggs_price = 0
            if not form.qty_single_eggs_remaining:
                form.qty_single_eggs_remaining = 0
            if not form.qty_single_eggs_added:
                form.qty_single_eggs_added = 0
            if not form.qty_half_dozen_egg_boxes_remaining:
                form.qty_half_dozen_egg_boxes_remaining = 0
            if not form.qty_half_dozen_egg_boxes_added:
                form.qty_half_dozen_egg_boxes_added = 0
            if not form.qty_ten_egg_boxes_remaining:
                form.qty_ten_egg_boxes_remaining = 0
            if not form.qty_ten_egg_boxes_added:
                form.qty_ten_egg_boxes_added = 0
            if not form.qty_dozen_egg_boxes_remaining:
                form.qty_dozen_egg_boxes_remaining = 0
            if not form.qty_dozen_egg_boxes_added:
                form.qty_dozen_egg_boxes_added = 0
            if not form.qty_trays_of_eggs_remaining:
                form.qty_trays_of_eggs_remaining = 0
            if not form.qty_trays_of_eggs_added:
                form.qty_trays_of_eggs_added = 0
            if not form.amount_paid_eggs_roadside:
                form.amount_paid_eggs_roadside = 0
            # Below temporarily removed as involves a more complex wiring
            # if not form.sales_amount_eggs_roadside:
            #     form.sales_amount_eggs_roadside = 0
            # form.sales_paid_difference_eggs_roadside = (tbc)
            if not form.loses_eggs_roadside:
                form.loses_eggs_roadside = 0

            form.save()  # Save the form fully
            return HttpResponseRedirect('/sales_and_income')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = EggRoadsideSalesForm
        template = 'sales_and_income/egg_roadside_sales.html'
        context = {'form': form}
        return render(request, template, context)


@login_required
def egg_delivery_sales_dashboard(request):
    """egg delivery sales dashboard view"""
    if request.POST:
        form = EggDeliverySalesDashboardForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form cleaned date =", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.

            if not form.breakages_and_loses_eggs_delivery:
                form.breakages_and_loses_eggs_delivery = 0
            form.save()  # Save the form fully
            return HttpResponseRedirect('/sales_and_income')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = EggDeliverySalesDashboardForm
        template = 'sales_and_income/egg_delivery_sales_dashboard.html'
        context = {'form': form}
        return render(request, template, context)


@login_required
def egg_delivery_sales(request):
    """view to egg delivery sales"""
    if request.POST:
        form = EggDeliverySalesForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form cleaned date =", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not form.qty_sold_eggs_delivery:
                form.qty_sold_eggs_delivery = 0
            if not form.qty_given_free_eggs_delivery:
                form.qty_given_free_eggs_delivery = 0
            if not form.amount_paid_eggs_delivery:
                form.amount_paid_eggs_delivery = 0

            form.save()  # Save the form fully
            return HttpResponseRedirect('/sales_and_income')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = EggDeliverySalesForm
        template = 'sales_and_income/egg_delivery_sales.html'
        context = {'form': form}
        return render(request, template, context)


# @login_required
# def egg_collection_sales_dashboard(request):
#     """egg collection sales dashboard view"""
#     if request.POST:
#         date = request.POST['date']
#         breakages_and_loses_eggs_collection = request.POST['breakages_and_loses_eggs_collection']
#         userprofile = UserProfile.objects.get(user=request.user)
#         farmprofile = userprofile.farmprofiles.all()
#         template = 'sales_and_income/egg_collection_sales_dashboard.html'
#     else:
#         form = EggcollectionSalesFormDashboard
#         userprofile = UserProfile.objects.get(user=request.user)
#         farmprofile = userprofile.farmprofiles.all()
#         template = 'sales_and_income/egg_collection_sales_dashboard.html'
#         context = {'form': form}
#         return render(request, template, context)


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
