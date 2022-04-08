from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from .forms import EggRoadsideSalesForm, EggCollectionSalesForm, EggDeliverySalesDashboardForm, EggDeliverySalesForm, EggMarketSalesForm, PricingForm, CustomerForm # EggCollectionSalesDashboardForm
from .models import Pricing, SalesType, EggRoadsideSales, Customer
import datetime
import decimal


@login_required
def sales_and_income(request):
    """sales & Income View"""
    template = 'sales_and_income/sales_and_income.html'
    context = {}
    return render(request, template, context)


class CreateRecentRoadsideSale:
    def __init__(self):
        self.qty_single_eggs_in_stock = 0
        self.qty_half_dozen_egg_boxes_in_stock = 0
        self.qty_ten_egg_boxes_in_stock = 0
        self.qty_dozen_egg_boxes_in_stock = 0
        self.qty_trays_eggs_in_stock = 0


@login_required
def egg_roadside_sales(request):
    """view to roadside sales"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    trays_quantity = farmprofile[0].trays_quantity
    sales_type = SalesType.objects.get(type='roadside')
    prices = Pricing.objects.filter(farm_profile=farmprofile[0]).filter(sales_type=sales_type).last()
    roadside_sale = EggRoadsideSales.objects.filter(farm_profile=farmprofile[0]).last()
    previous_sale = True
    if not roadside_sale:
        previous_sale = False
        # roadside_sale = CreateRecentRoadsideSale()
    if request.POST:
        pricing_form = PricingForm(request.POST, instance=prices)
        sales_form = EggRoadsideSalesForm(request.POST, request.FILES, instance=roadside_sale)
        previous_roadside_sale = EggRoadsideSales.objects.filter(farm_profile=farmprofile[0]).last()
        if sales_form.is_valid() and pricing_form.is_valid():
            print("pricing_form = ", pricing_form.cleaned_data)
            print("sales_form = ", sales_form.cleaned_data)
            if pricing_form.has_changed():
                print("Changed")
                prices = Pricing(
                    farm_profile=farmprofile[0],
                    sales_type=sales_type,
                    single_egg_price=pricing_form.cleaned_data['single_egg_price'],
                    half_dozen_eggs_price=pricing_form.cleaned_data['half_dozen_eggs_price'],
                    ten_eggs_price=pricing_form.cleaned_data['ten_eggs_price'],
                    dozen_eggs_price=pricing_form.cleaned_data['dozen_eggs_price'],
                    trays_of_eggs_price=pricing_form.cleaned_data['trays_of_eggs_price'],
                )
                prices.save()
                print("prices = ", prices)
            sales_form = sales_form.save(commit=False)
            sales_form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value
            sales_form.pricing = prices
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not roadside_sale:
                sales_form.save()
            else:
                print("roadside_sale = ", roadside_sale.qty_single_eggs_in_stock)
                # Calculations for eggs sold
                if previous_roadside_sale.qty_single_eggs_in_stock is not None:
                    sales_form.qty_single_eggs_sold = previous_roadside_sale.qty_single_eggs_in_stock - sales_form.qty_single_eggs_remaining
                else:
                    sales_form.qty_single_eggs_sold = 0
                if previous_roadside_sale.qty_half_dozen_egg_boxes_in_stock is not None:
                    sales_form.qty_half_dozen_egg_boxes_sold = previous_roadside_sale.qty_half_dozen_egg_boxes_in_stock - sales_form.qty_half_dozen_egg_boxes_remaining
                else:
                    sales_form.qty_half_dozen_egg_boxes_sold = 0
                if previous_roadside_sale.qty_ten_egg_boxes_in_stock is not None:
                    sales_form.qty_ten_egg_boxes_sold = previous_roadside_sale.qty_ten_egg_boxes_in_stock - sales_form.qty_ten_egg_boxes_remaining
                else:
                    sales_form.qty_ten_egg_boxes_sold = 0
                if previous_roadside_sale.qty_dozen_egg_boxes_in_stock is not None:
                    sales_form.qty_dozen_egg_boxes_sold = previous_roadside_sale.qty_dozen_egg_boxes_in_stock - sales_form.qty_dozen_egg_boxes_remaining
                else:
                    sales_form.qty_dozen_egg_boxes_sold = 0
                if previous_roadside_sale.qty_trays_eggs_in_stock is not None:
                    sales_form.qty_trays_eggs_sold = previous_roadside_sale.qty_trays_eggs_in_stock - sales_form.qty_trays_eggs_remaining
                else:
                    sales_form.qty_trays_eggs_sold = 0
                # Calculations for updating eggs in stock for the next sale
                next_roadside_sale = {}
                # Single eggs
                if sales_form.qty_single_eggs_in_stock is not None:
                    next_roadside_sale['qty_single_eggs_in_stock'] = sales_form.qty_single_eggs_in_stock
                else:
                    next_roadside_sale['qty_single_eggs_in_stock'] = None
                if previous_roadside_sale.qty_single_eggs_in_stock is not None:
                    next_roadside_sale['qty_single_eggs_in_stock'] = previous_roadside_sale.qty_single_eggs_in_stock \
                                                                     - sales_form.qty_single_eggs_sold \
                                                                     + sales_form.qty_single_eggs_added
                    sales_form.qty_single_eggs_in_stock = previous_roadside_sale.qty_single_eggs_in_stock
                    if next_roadside_sale['qty_single_eggs_in_stock'] == 0:
                        next_roadside_sale['qty_single_eggs_in_stock'] = None
                # 6/12 eggs
                if sales_form.qty_half_dozen_egg_boxes_in_stock is not None:
                    next_roadside_sale['qty_half_dozen_egg_boxes_in_stock'] = sales_form.qty_half_dozen_egg_boxes_in_stock
                else:
                    next_roadside_sale['qty_half_dozen_egg_boxes_in_stock'] = None
                if previous_roadside_sale.qty_half_dozen_egg_boxes_in_stock is not None:
                    next_roadside_sale['qty_half_dozen_egg_boxes_in_stock'] = previous_roadside_sale.qty_half_dozen_egg_boxes_in_stock \
                                                                              - sales_form.qty_half_dozen_egg_boxes_sold \
                                                                              + sales_form.qty_half_dozen_egg_boxes_added
                    sales_form.qty_half_dozen_egg_boxes_in_stock = previous_roadside_sale.qty_half_dozen_egg_boxes_in_stock
                    if next_roadside_sale['qty_half_dozen_egg_boxes_in_stock'] == 0:
                        next_roadside_sale['qty_half_dozen_egg_boxes_in_stock'] = None
                # 10 eggs
                if sales_form.qty_ten_egg_boxes_in_stock is not None:
                    next_roadside_sale['qty_ten_egg_boxes_in_stock'] = sales_form.qty_ten_egg_boxes_in_stock
                else:
                    next_roadside_sale['qty_ten_egg_boxes_in_stock'] = None
                if previous_roadside_sale.qty_ten_egg_boxes_in_stock is not None:
                    next_roadside_sale['qty_ten_egg_boxes_in_stock'] = previous_roadside_sale.qty_ten_egg_boxes_in_stock \
                                                                       - sales_form.qty_ten_egg_boxes_sold \
                                                                       + sales_form.qty_ten_egg_boxes_added
                    sales_form.qty_ten_egg_boxes_in_stock = previous_roadside_sale.qty_ten_egg_boxes_in_stock
                    if next_roadside_sale['qty_ten_egg_boxes_in_stock'] == 0:
                        next_roadside_sale['qty_ten_egg_boxes_in_stock'] = None
                # 12/12 eggs
                if sales_form.qty_dozen_egg_boxes_in_stock is not None:
                    next_roadside_sale['qty_dozen_egg_boxes_in_stock'] = sales_form.qty_dozen_egg_boxes_in_stock
                else:
                    next_roadside_sale['qty_dozen_egg_boxes_in_stock'] = None
                if previous_roadside_sale.qty_dozen_egg_boxes_in_stock is not None:
                    next_roadside_sale['qty_dozen_egg_boxes_in_stock'] = previous_roadside_sale.qty_dozen_egg_boxes_in_stock \
                                                                       - sales_form.qty_dozen_egg_boxes_sold \
                                                                       + sales_form.qty_dozen_egg_boxes_added
                    sales_form.qty_dozen_egg_boxes_in_stock = previous_roadside_sale.qty_dozen_egg_boxes_in_stock
                    if next_roadside_sale['qty_dozen_egg_boxes_in_stock'] == 0:
                        next_roadside_sale['qty_dozen_egg_boxes_in_stock'] = None
                # Trays eggs
                if sales_form.qty_trays_eggs_in_stock is not None:
                    next_roadside_sale['qty_trays_eggs_in_stock'] = sales_form.qty_trays_eggs_in_stock
                else:
                    next_roadside_sale['qty_trays_eggs_in_stock'] = None
                if previous_roadside_sale.qty_trays_eggs_in_stock is not None:
                    next_roadside_sale['qty_trays_eggs_in_stock'] = previous_roadside_sale.qty_trays_eggs_in_stock \
                                                                       - sales_form.qty_trays_eggs_sold \
                                                                       + sales_form.qty_trays_eggs_added
                    sales_form.qty_trays_eggs_in_stock = previous_roadside_sale.qty_trays_eggs_in_stock
                    if next_roadside_sale['qty_trays_eggs_in_stock'] == 0:
                        next_roadside_sale['qty_trays_eggs_in_stock'] = None

                # Calculations for income
                print("single_egg_price = ", prices.single_egg_price)
                print("half_dozen_eggs_price = ", prices.half_dozen_eggs_price)
                print("ten_eggs_price = ", prices.ten_eggs_price)
                print("dozen_eggs_price = ", prices.dozen_eggs_price)
                print("trays_of_eggs_price = ", prices.trays_of_eggs_price)
                print("sales_form.qty_dozen_egg_boxes_sold = ", sales_form.qty_dozen_egg_boxes_sold)
                if prices.single_egg_price is None:
                    prices.single_egg_price = 0
                if prices.half_dozen_eggs_price is None:
                    prices.half_dozen_eggs_price = 0
                if prices.ten_eggs_price is None:
                    prices.ten_eggs_price = 0
                if prices.dozen_eggs_price is None:
                    prices.dozen_eggs_price = 0
                if prices.trays_of_eggs_price is None:
                    prices.trays_of_eggs_price = 0
                if sales_form.losses_eggs_roadside is None:
                    sales_form.losses_eggs_roadside = 0
                suggested_income = (sales_form.qty_single_eggs_sold * decimal.Decimal(prices.single_egg_price)) \
                    + (sales_form.qty_half_dozen_egg_boxes_sold * decimal.Decimal(prices.half_dozen_eggs_price)) \
                    + (sales_form.qty_ten_egg_boxes_sold * decimal.Decimal(prices.ten_eggs_price)) \
                    + (sales_form.qty_dozen_egg_boxes_sold * decimal.Decimal(prices.dozen_eggs_price)) \
                    + (sales_form.qty_trays_eggs_sold * decimal.Decimal(prices.trays_of_eggs_price))
                sales_form.income_deficit = sales_form.income - suggested_income + (sales_form.losses_eggs_roadside * decimal.Decimal(prices.single_egg_price))
                sales_form.pricing = prices
                print("suggested_income = ", suggested_income)
                print("sales_form.income_deficit = ", sales_form.income_deficit)
                sales_form.save()
                next_object = EggRoadsideSales(
                    farm_profile=farmprofile[0],
                    date=datetime.datetime.now(),
                    qty_single_eggs_in_stock=next_roadside_sale['qty_single_eggs_in_stock'],
                    qty_half_dozen_egg_boxes_in_stock=next_roadside_sale['qty_half_dozen_egg_boxes_in_stock'],
                    qty_ten_egg_boxes_in_stock=next_roadside_sale['qty_ten_egg_boxes_in_stock'],
                    qty_dozen_egg_boxes_in_stock=next_roadside_sale['qty_dozen_egg_boxes_in_stock'],
                    qty_trays_eggs_in_stock=next_roadside_sale['qty_trays_eggs_in_stock'],
                    pricing=prices
                )
                next_object.save()
            # farm = farmprofile[0]  # Refer to the farmprofile object which is obtained above
            # farm.eggs_in_stock -= form.qty_saleable_eggs  # Update the eggs_in_stock value to itself
            # farm.save()  # Save the farmprofile to the db.

            return HttpResponseRedirect('/sales_and_income')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        pricing_form = PricingForm(instance=prices)
        sales_form = EggRoadsideSalesForm(instance=roadside_sale)
        template = 'sales_and_income/egg_roadside_sales.html'
        context = {'pricing_form': pricing_form,
                   'sales_form': sales_form,
                   'previous_sale': previous_sale}
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
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    customers = Customer.objects.filter(farm_profile=farmprofile[0])
    print("customers = ", customers)
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
        context = {'form': form,
                   'customers': customers}
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


@login_required
def customer(request):
    """view to collection sales"""
    if request.POST:
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form cleaned date =", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.

            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not form.single_egg_price:
                form.single_egg_price = 0
            if not form.six_egg_price:
                form.six_egg_price = 0
            if not form.ten_egg_price:
                form.ten_egg_price = 0
            if not form.twelve_egg_price:
                form.twelve_egg_price = 0
            if not form.tray_price:
                form.tray_price = 0
            form.save()  # Save the form fully
            return HttpResponseRedirect('/customer')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = CustomerForm
        template = 'sales_and_income/customer.html'
        context = {'form': form}
        return render(request, template, context)
