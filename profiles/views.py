from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from .models import UserProfile, FarmProfile, FarmType, Breed, FarmPurpose
from flock_management.models import Flocks, Coops
from health_and_welfare.models import Supplements, SupplementsName
from regular_tasks.models import Feeds
from backyard_chicken_manager.settings import BCM_MAPS_KEY


# Create your views here.
@login_required
def dashboard(request):
    '''Render User dashboard'''
    # 1. Try to get the userprofile from the UserProfile model
    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        return redirect(onboard_personal)
    # 2. Try to get the farmprofile for the user
    try:
        farmprofile = userprofile.farmprofiles.all()
    # 3. Check the onboard_complete field of the farmprofile
        if not farmprofile:
            return redirect(onboard_personal)
        else:
            request.session['onboard_profile_data'] = {}
            context = {
                'userprofile': userprofile,
                'farmprofile': farmprofile,
            }
            template = 'profiles/dashboard.html'
            return render(request, template, context)
    except ObjectDoesNotExist:
        return redirect(onboard_personal)


@login_required
def get_onboarding_data(request):
    """This function handles the forms during the onboarding process. It saves the
    form data to a session variable called onboarding_profile_data"""
    # Get the session onboard_profile_data dictionary or create an empty /
    # dictionary if none is already created"""
    onboard_profile_data = request.session.get('onboard_profile_data', {})
    # Get the form data
    raw_form_data = request.POST
    print("raw_form_data = ", raw_form_data)
    # Declare a white list of field names as a filter prior to processing /
    # the raw_form_data to the session onboard_profile_data. This will allow /
    # only certain fields to be saved to the session and will exclude all /
    # others including the csrf_token and redirect_url values
    white_list = [
        'full_name',
        'city_country',
        'farm_business_name',
        'farm_type',
        'flock_qty',
        'coop_qty',
        'flock_name',
        'acquired_date',
        'coop_name',
        'breed',
        'hens_qty',
        'chicks_qty',
        'cocks_qty',
        'trays_qty',
        'feed_name',
        'saleable_eggs_qty',
        'feed_qty_stock',
        'supplement_name',
        'supplement_amount_stock'
    ]

    # Declare a list of the fields that require integers in order to format /
    # particular session values in integer form.
    integer_fields = [
        'farm_type',
        'breed',
        'flock_qty',
        'coop_qty',
        'hens_qty',
        'chicks_qty',
        'cocks_qty',
        'trays_qty',
        'saleable_eggs_qty',
        'feed_qty_stock',
        'supplement_amount_stock'
    ]

    checkbox_fields = [
        'roadside_check',
        'markets_check',
        'deliveries_check',
        'collections_check',
        'single_eggs_check',
        'half_dozen_carton_check',
        'dozen_carton_check',
        'trays_check',
    ]

    # Declare a dictionary to contain the cleaned submitted form data
    cleaned_form_data = {}

    if 'checkbox_form' in raw_form_data:
        for key in checkbox_fields:
            if key in request.POST:
                cleaned_form_data[key] = True
            else:
                cleaned_form_data[key] = False
    # Run the raw_form_data against the list of items in the white list
    for key, val in raw_form_data.items():
        if key in white_list:
            # Check if it requires the value to be an integer field
            if key in integer_fields:
                if val == '':
                    cleaned_form_data[key] = 0
                    # if Y: write the values as int
                else:
                    cleaned_form_data[key] = int(request.POST[key])
            else:
                # Else N: write the value as is.
                cleaned_form_data[key] = request.POST[key]

    # Process the cleaned_form_data to the session onboard_profile_data /
    # to add or update keys and values with each form submit
    for key, val in cleaned_form_data.items():
        onboard_profile_data.update({key: val})
    print('onboard_profile_data = ', onboard_profile_data)

    # Function to add onboard_profile_data to the db
    if 'onboarding_finish' in raw_form_data:
        user = CustomUser.objects.get(email=request.user)
        full_name = onboard_profile_data['full_name'].split()
        first_name = full_name[0]
        last_name = ''
        for item in full_name[1:]:
            last_name += item + ' '
        city_country = onboard_profile_data['city_country']
        # Check if a UserProfile exists for this User
        try:
            userprofile = UserProfile.objects.get(user=request.user)
            userprofile.first_name = first_name
            userprofile.last_name = last_name
            userprofile.city_country = city_country
            userprofile.save()
        except ObjectDoesNotExist:
            # Create a new UserProfile for this User
            userprofile = UserProfile(
                user=user,
                first_name=first_name,
                last_name=last_name,
                city_country=city_country
            )
            userprofile.save()
        # Create a new FarmProfile
        user = userprofile.id
        farm_business_name = onboard_profile_data['farm_business_name']
        farm_type = FarmType(pk=onboard_profile_data['farm_type'])
        farmprofile = FarmProfile(
            user_profile=userprofile,
            farm_business_name=farm_business_name,
            farm_type=farm_type,
            farm_sales_roadside=onboard_profile_data['roadside_check'],
            farm_sales_markets=onboard_profile_data['markets_check'],
            farm_sales_deliveries=onboard_profile_data['deliveries_check'],
            farm_sales_collections=onboard_profile_data['collections_check'],
            sales_units_single_eggs=onboard_profile_data['single_eggs_check'],
            sales_units_half_dozen_carton=onboard_profile_data['half_dozen_carton_check'],
            sales_units_dozen_carton=onboard_profile_data['dozen_carton_check'],
            sales_units_trays=onboard_profile_data['trays_check'],
            trays_quantity=onboard_profile_data['trays_qty'],
            eggs_in_stock=onboard_profile_data['saleable_eggs_qty']
        )
        farmprofile.save()
        # Create a new Coop entry
        coop = Coops(
            farm_profile=farmprofile,
            coop_name=onboard_profile_data['coop_name']
        )
        coop.save()
        # Create a new Flocks entry
        breed = Breed(pk=onboard_profile_data['breed'])
        flock = Flocks(
            farm_profile=farmprofile,
            breed=breed,
            flock_name=onboard_profile_data['flock_name'],
            hens_qty=onboard_profile_data['hens_qty'],
            chicks_qty=onboard_profile_data['chicks_qty'],
            cocks_qty=onboard_profile_data['cocks_qty']
        )
        flock.save()
        flock.coop.add(coop)
        # supplement = SupplementsName(
        #     farm_profile=farmprofile,
        #     supplement_name=onboard_profile_data['supplement_name'],
        #     supplement_in_stock=onboard_profile_data['supplement_amount_stock'],
        # )
        # supplement.save()
        feed = Feeds(
            farm_profile=farmprofile,
            feed_name=onboard_profile_data['feed_name'],
            qty_food=onboard_profile_data['feed_qty_stock']
        )
        feed.save()
        farmprofile.onboard_complete = True
        farmprofile.save()
        return redirect(dashboard)

    request.session['onboard_profile_data'] = onboard_profile_data
    # Read the redirect_url value from the form data and redirect user to next page
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)


@login_required
def onboard_personal(request):
    '''Render onboarding step 1'''
    # Get the session onboard_profile_data dictionary or create an empty /
    # dictionary if none is already created"""
    onboard_profile_data = request.session.get('onboard_profile_data', {})
    # For returning users with deleted FarmProfiles
    try:
        userprofile = UserProfile.objects.get(user=request.user)
        onboard_profile_data['full_name'] = userprofile.first_name + ' ' + userprofile.last_name
        onboard_profile_data['city_country'] = userprofile.city_country
    except ObjectDoesNotExist:
        print("UserProfile does not exists")
    # Reload the new onboard_profile_data back to the session variable
    request.session['onboard_profile_data'] = onboard_profile_data
    farm_types = FarmType.objects.all()
    for farm_type in farm_types:
        farm_type = str(farm_type)
    context = {
        "farm_types": farm_types,
        "google_maps_api": f"https://maps.googleapis.com/maps/api/js?key={BCM_MAPS_KEY}&libraries=places&callback=initAutocomplete"
    }
    template = 'profiles/onboard_personal.html'
    return render(request, template, context)


@login_required
def onboard_flock(request):
    '''Render onboarding step 3'''
    breed = Breed.objects.all()
    for item in breed:
        item = str(item)
    purpose = FarmPurpose.objects.all()

    context = {
        'breed': breed,
        'purpose': purpose
    }
    template = 'profiles/onboard_flock.html'
    return render(request, template, context)


@login_required
def onboard_sales(request):
    '''Render onboarding step 4'''
    context = {

    }
    template = 'profiles/onboard_sales.html'
    return render(request, template, context)


@login_required
def onboard_stock(request):
    '''Render onboarding step 5'''
    context = {

    }
    template = 'profiles/onboard_stock.html'
    return render(request, template, context)
