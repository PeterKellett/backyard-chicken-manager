from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from .forms import EggRoadsideSalesForm, EggCollectionSalesForm, EggDeliverySalesDashboardForm, EggDeliverySalesForm, EggMarketSalesForm, PricingForm # EggCollectionSalesDashboardForm
from .models import Pricing, EggRoadsideSales


@login_required
def sales_and_income(request):
    """sales & Income View"""
    template = 'sales_and_income/sales_and_income.html'
    context = {}
    return render(request, template, context)


@login_required
def egg_roadside_sales(request):
    """view to roadside sales"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    trays_quantity = farmprofile[0].trays_quantity
    prices = Pricing.objects.filter(farm_profile=farmprofile[0]).filter(sales_type=1)
    roadside_sale_history = EggRoadsideSales.objects.filter(farm_profile=farmprofile[0])
    if roadside_sale_history.exists():
        print("NONE")
        recent_roadside_sale = {}
        recent_roadside_sale['qty_single_eggs_added'] = 0
    else:
        recent_roadside_sale = roadside_sale_history[:1]
    print("recent_roadside_sale = ", recent_roadside_sale)
    # print("prices = ", prices)
    # print("prices[0] = ", prices[0].id)
    # print("dir prices[0] = ", dir(prices[0]))
    if request.POST:
        sales_form = EggRoadsideSalesForm(request.POST, request.FILES)
        pricing_form = PricingForm(request.POST, instance=prices[0])
        # print("sales_form = ", sales_form)
        # print("pricing_form = ", pricing_form)
        if sales_form.is_valid() and pricing_form.is_valid():
            print(("sales_form cleaned data =", sales_form.cleaned_data))
            print(("pricing_form cleaned data =", pricing_form.cleaned_data))
            prices = pricing_form.save()  # Presave the form values to create an instance of the model but don't commit to db.
            sales_form = sales_form.save(commit=False)
            sales_form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not sales_form.qty_single_eggs_remaining:
                sales_form.qty_single_eggs_remaining = 0
            if not sales_form.qty_single_eggs_added:
                sales_form.qty_single_eggs_added = 0
            if not sales_form.qty_half_dozen_egg_boxes_remaining:
                sales_form.qty_half_dozen_egg_boxes_remaining = 0
            if not sales_form.qty_half_dozen_egg_boxes_added:
                sales_form.qty_half_dozen_egg_boxes_added = 0
            if not sales_form.qty_ten_egg_boxes_remaining:
                sales_form.qty_ten_egg_boxes_remaining = 0
            if not sales_form.qty_ten_egg_boxes_added:
                sales_form.qty_ten_egg_boxes_added = 0
            if not sales_form.qty_dozen_egg_boxes_remaining:
                sales_form.qty_dozen_egg_boxes_remaining = 0
            if not sales_form.qty_dozen_egg_boxes_added:
                sales_form.qty_dozen_egg_boxes_added = 0
            if not sales_form.qty_trays_eggs_remaining:
                sales_form.qty_trays_eggs_remaining = 0
            if not sales_form.qty_trays_eggs_added:
                sales_form.qty_trays_eggs_added = 0
            #sales_form.qty_single_eggs_sold = recent_roadside_sale.qty_single_eggs_added - sales_form.qty_single_eggs_remaining
            if not sales_form.income:
                sales_form.income = 0
            # Below temporarily removed as involves a more complex wiring
            # if not form.sales_amount_eggs_roadside:
            #     form.sales_amount_eggs_roadside = 0
            # form.sales_paid_difference_eggs_roadside = (tbc)
            if not sales_form.loses_eggs_roadside:
                sales_form.loses_eggs_roadside = 0
            sales_form.save()

            # farm = farmprofile[0]  # Refer to the farmprofile object which is obtained above
            # farm.eggs_in_stock -= form.qty_saleable_eggs  # Update the eggs_in_stock value to itself
            # farm.save()  # Save the farmprofile to the db.

            return HttpResponseRedirect('/sales_and_income')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        pricing_form = PricingForm(instance=prices[0])
        sales_form = EggRoadsideSalesForm
        template = 'sales_and_income/egg_roadside_sales.html'
        context = {'pricing_form': pricing_form,
                   'sales_form': sales_form}
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
    """view to delivery sales"""
    # userprofile = UserProfile.objects.get(user=request.user)
    # farmprofile = userprofile.farmprofiles.all()
    # print(farmprofile)
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
    """view to collection sales"""
    if request.POST:
        form = EggCollectionSalesForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form cleaned date =", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not form.qty_sold_eggs_collection:
                form.qty_sold_eggs_collection = 0
            if not form.qty_given_free_eggs_collection:
                form.qty_given_free_eggs_collection = 0
            if not form.amount_paid_eggs_collection:
                form.amount_paid_eggs_collection = 0
            if not form.breakages_and_loses_eggs_collection:
                form.breakages_and_loses_eggs_collection = 0
            form.save()  # Save the form fully
            return HttpResponseRedirect('/sales_and_income')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = EggCollectionSalesForm
        template = 'sales_and_income/egg_collection_sales.html'
        context = {'form': form}
        return render(request, template, context)


@login_required
def egg_market_sales(request):
    """view to Market sales"""
    # userprofile = UserProfile.objects.get(user=request.user)
    # farmprofile = userprofile.farmprofiles.all()
    # print(farmprofile)
    if request.POST:
        form = EggMarketSalesForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form cleaned date =", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            # form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value

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
            if not form.qty_single_eggs_sold:
                form.qty_single_eggs_sold = 0
            if not form.qty_half_dozen_egg_boxes_sold:
                form.qty_half_dozen_egg_boxes_sold = 0
            if not form.qty_ten_egg_boxes_sold:
                form.qty_ten_egg_boxes_sold = 0
            if not form.qty_dozen_egg_boxes_sold:
                form.qty_dozen_egg_boxes_sold = 0
            if not form.qty_trays_of_eggs_sold:
                form.qty_trays_of_eggs_sold = 0
            if not form.amount_paid_eggs_market:
                form.amount_paid_eggs_market = 0
            if not form.loses_eggs_market:
                form.loses_eggs_market = 0
            form.save()
            # userprofile = UserProfile.objects.get(user=request.user)
            # farmprofile = userprofile.farmprofiles.all()
            return HttpResponseRedirect('/sales_and_income')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = EggMarketSalesForm
        # userprofile = UserProfile.objects.get(user=request.user)
        # farmprofile = userprofile.farmprofiles.all()
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
