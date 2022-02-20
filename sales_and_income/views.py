from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser


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
    template = 'sales_and_income/roadside_sales.html'
    context = {}
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
