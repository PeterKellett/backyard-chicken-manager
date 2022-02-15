from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customAuth.models import CustomUser
from .models import UserProfile, FarmProfile, FarmType, Breed, FarmPurpose


# Create your views here.
@login_required
def dashboard(request):
    '''Render User dashboard'''
    context = {

    }
    template = 'profiles/dashboard.html'
    return render(request, template, context)


@login_required
def get_onboarding_data(request):
    """This function handles the forms during the onboarding process. It saves the
    form data to a session variable called onboarding_profile_data"""
    # Get the session onboard_profile_data dictionary or create an empty /
    # dictionary if none is already created"""
    onboard_profile_data = request.session.get('onboard_profile_data', {})

    # Get the form data
    raw_form_data = request.POST

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
        'purpose',
        'all_hens_check',
        'hens_qty',
        'all_chicks_check',
        'chicks_qty',
        'all_cocks_check',
        'cocks_qty'
    ]

    # Declare a list of the fields that require integers in order to format /
    # particular session values in integer form.
    integer_fields = [
        'farm_type',
        'flock_qty',
        'coop_qty',
        'hens_qty',
        'chicks_qty',
        'cocks_qty'
    ]

    # Declare a dictionary to contain the cleaned submitted form data
    cleaned_form_data = {}

    # Run the raw_form_data against the list of items in the white list
    for key in raw_form_data:
        if key in white_list:
            # Check if it requires the value to be an integer field
            if key in integer_fields:
                # if Y: write the values as int
                cleaned_form_data[key] = int(request.POST[key])
            else:
                # Else N: write the value as is.
                cleaned_form_data[key] = request.POST[key]

    # Process the cleaned_form_data to the session onboard_profile_data /
    # to add or update keys and values with each form submit
    for key, val in cleaned_form_data.items():
        onboard_profile_data.update({key: val})
    print('onboard_profile_data = ', onboard_profile_data)

    # Reload the new onboard_profile_data back to the session variable
    request.session['onboard_profile_data'] = onboard_profile_data

    # Read the redirect_url value from the form data and redirect user to next page
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)


@login_required
def onboard_personal(request):
    '''Render onboarding step 1'''
    # profile = get_object_or_404(CustomUser, email=request.user)
    # if request.method == 'POST':
    #     full_name = request.POST.get('full_name').split()
    #     print("full_name = ", full_name)
    #     print("profile = ", profile)
    #     first_name = full_name[0]
    #     if len(full_name) > 2:
    #         print("no name")
    #     last_name = 'smith'
    #     userprofile = UserProfile(
    #         user=profile,
    #         first_name=first_name,
    #         last_name=last_name,
    #     )
    #     userprofile.save()
    farm_types = FarmType.objects.all()
    print(farm_types)
    for farm_type in farm_types:
        farm_type = str(farm_type)
        # print(farm_type)
        # print(type(farm_type))

    context = {
        "farm_types": farm_types
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
