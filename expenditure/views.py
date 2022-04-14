from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from profiles.models import FarmProfile, UserProfile
from .forms import PurchasesCategoryForm, PurchasesForm, WithdrawalsForm
from .models import PaymentMethods, PurchasesCategory, Purchases, Withdrawals
import json


def get_payment_methods(request):
    """view to current flock"""
    payment_method = PaymentMethods.objects.values('category')
    return JsonResponse({"payment_method": list(payment_method)}, safe=False)


def get_purchase_categories(request):
    """view to current flock"""
    categories = PurchasesCategory.objects.values('category')
    return JsonResponse({"categories": list(categories)}, safe=False)


def purchases(request):
    """view to current flock"""
    category = PurchasesCategory.objects.all()
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        form = PurchasesForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form.cleaned_data = ", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value
            print("form farm profile :", form.farm_profile)
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not form.total_cost:
                form.total_cost = 0
            form.save()  # Save the form fully.
            farm = farmprofile[0]  # Refer to the farmprofile object which is obtained above
            farm.save()  # Save the farmprofile to the db.
            return HttpResponseRedirect('/expenditure/')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = PurchasesForm
        flock = farmprofile[0].flocks.all()
        print("flock = ", flock)
        template = 'expenditure/purchases.html'
        context = {'form': form,
                   'category': category,
                   'flocks': flock}
        print("context :", type(context))
        return render(request, template, context)


# def withdrawals(request):
#     """view to current flock"""
#     # The three lines below can be deleted once the rest of the code has 
#     # been uncommented and implemented
#     template = 'expenditure/withdrawals.html'
#     context = {}
#     return render(request, template, context)


def withdrawals(request):
    """view to current flock"""
    userprofile = UserProfile.objects.get(user=request.user)
    farmprofile = userprofile.farmprofiles.all()
    if request.POST:
        form = WithdrawalsForm(request.POST, request.FILES)
        if form.is_valid():
            print(("form.cleaned_data = ", form.cleaned_data))
            form = form.save(commit=False)  # Presave the form values to create an instance of the model but don't commit to db.
            form.farm_profile = farmprofile[0]  # Add in the farmprofile ForeignKey value
            print("form farm profile :", form.farm_profile)
            # Manual check of integer fields is required here to set field variables to 0 if NoneType or '' is returned /
            # because setting the model default = 0 affects floating labels.
            if not form.total_cost:
                form.total_cost = 0
            form.save()  # Save the form fully.
            farm = farmprofile[0]  # Refer to the farmprofile object which is obtained above
            farm.save()  # Save the farmprofile to the db.
            return HttpResponseRedirect('/expenditure/withdrawals')  # Returning a HttpResponseRedirect is required with Django and then simply redirect to required view in the ()
    else:
        form = WithdrawalsForm
        flock = farmprofile[0].flocks.all()
        print("flock = ", flock)
        template = 'expenditure/withdrawals.html'
        context = {'form': form,
                   'flocks': flock}
        print("context :", type(context))
        return render(request, template, context)
