from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from .models import UserProfile, FarmProfile, FarmType


# Create your views here.
@login_required
def dashboard(request):
    '''Render User dashboard'''
    context = {

    }
    template = 'profiles/dashboard.html'
    return render(request, template, context)



def get_onboarding_data(request):
    """This function handles the forms during the onboarding process. It saves the
    form data to a session variable called onboarding_profile_data"""
    # Get the session profile data or create an empty dictionary if none /
    # is already created"""
    onboard_profile_data = request.session.get('onboard_profile_data',
                                               {
                                                    'full_name': '',
                                                    'city_country': '',
                                                    'farm_business_name': '',
                                                    'farm_type': '',
                                                    'flock_qty': '',
                                                    'coop_qty': '',
                                                    'flock_name': '',
                                                    'acquired_date': '',
                                                    'breed': '',
                                                    'purpose': '',
                                                    'all_hens_check': '',
                                                    'hens_qty': '',
                                                    'all_chicks_check': '',
                                                    'chicks_qty': '',
                                                    'all_cocks_check': '',
                                                    'cocks_qty': '',
                                                    'farm_sales_roadside': '',
                                                    'farm_sales_markets': '',
                                                    'farm_sales_deliveries': '',
                                                    'farm_sales_collections': '',
                                                    'eggs_in_stock': '',
                                                    'current_balance': ''
                                               })

    # onboard_profile_data = {
    #                             'full_name': '',
    #                             'city_country': '',
    #                             'farm_business_name': '',
    #                             'farm_type': '',
    #                             'flock_qty': '',
    #                             'coop_qty': '',
    #                             'flock_name': '',
    #                             'acquired_date': '',
    #                             'breed': '',
    #                             'purpose': '',
    #                             'all_hens_check': '',
    #                             'hens_qty': '',
    #                             'all_chicks_check': '',
    #                             'chicks_qty': '',
    #                             'all_cocks_check': '',
    #                             'cocks_qty': '',
    #                             'farm_sales_roadside': '',
    #                             'farm_sales_markets': '',
    #                             'farm_sales_deliveries': '',
    #                             'farm_sales_collections': '',
    #                             'eggs_in_stock': '',
    #                             'current_balance': ''
    #                         }
    
    # Get the form data
    for key in onboard_profile_data:
        print('key = ', key)
        if key in request.POST:
            if key in ('flock_qty', 'coop_qty'):
                onboard_profile_data[key] = int(request.POST[key])
            else:
                onboard_profile_data[key] = request.POST[key]
    redirect_url = request.POST.get('redirect_url')
    x = onboard_profile_data.values()
    print('x = ', x)
    request.session['onboard_profile_data'] = onboard_profile_data
    # print('onboard_profile_data = ', request.session['onboard_profile_data'])
    return redirect(redirect_url)


@login_required
def onboard_personal(request):
    '''Render onboarding step 1'''
    profile = get_object_or_404(CustomUser, email=request.user)
    if request.method == 'POST':
        full_name = request.POST.get('full_name').split()
        print("full_name = ", full_name)
        print("profile = ", profile)
        first_name = full_name[0]
        if len(full_name) > 2:
            print("no name")      
        last_name = 'smith'
        userprofile = UserProfile(
            user=profile,
            first_name=first_name,
            last_name=last_name,
        )
        # userprofile.save()

    context = {

    }
    template = 'profiles/onboard_personal.html'
    return render(request, template, context)


@login_required
def onboard_farm(request):
    '''Render onboarding step 2'''
    farm_types = FarmType.objects.all()
    for farm_type in farm_types:
        farm_type = str(farm_type)
        # print(farm_type)
        # print(type(farm_type))

    context = {
        "farm_types": farm_types
    }
    template = 'profiles/onboard_farm.html'
    return render(request, template, context)


@login_required
def onboard_flock(request):
    '''Render onboarding step 3'''
    context = {

    }
    template = 'profiles/onboard_flock.html'
    return render(request, template, context)


@login_required
def onboard_produce(request):
    '''Render onboarding step 4'''
    context = {

    }
    template = 'profiles/onboard_produce.html'
    return render(request, template, context)


@login_required
def onboard_stock(request):
    '''Render onboarding step 5'''
    context = {

    }
    template = 'profiles/onboard_stock.html'
    return render(request, template, context)
