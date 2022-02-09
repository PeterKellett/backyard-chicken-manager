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
                                                    
                                               })

    # Get the form data and quick test
    raw_form_data = request.POST
    print('form_data = ', raw_form_data)
    # Declare a list of field names to be removed from the raw_form_data
    hidden_list = [
        'csrfmiddlewaretoken',
        'redirect_url'
    ]
    # Declare a dictionary to contain the cleaned submitted form data
    cleaned_form_data = {}
    # Run the raw_form_data against the list of items in the hidden list to remove the forms hidden fields csrf and redirect_url data
    for key in raw_form_data:
        if key not in hidden_list:
            cleaned_form_data[key] = request.POST[key]  # Add key name and value from the form to the cleaned_form_data Variable
   
    # Process the cleaned_form_data to the session onboard_profile_data and add or update keys and values with each form submit
    for field in cleaned_form_data:  # for each field in the form
        print('field = ', field)
        if field in onboard_profile_data:  # Check if that key name is in the session vars already
            if field in ('flock_qty', 'coop_qty'):  # If Y: Check if this field is required to be an integer
                onboard_profile_data.update({field: int(request.POST[field])})  # If Y: Update the value as an int
            else:  # Else N
                onboard_profile_data.update({field: request.POST[field]})  # update as raw str
        else:
            if field in ('flock_qty', 'coop_qty'):  # Else N: Check if this field is required to be an integer
                onboard_profile_data[field] = int(request.POST[field])  # If Y: Add key and value as int
            else:
                onboard_profile_data[field] = request.POST[field]  # Else N: save as raw str
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
