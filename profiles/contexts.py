def onboarding_data(request):
    """This is the session variables which loaded
    with each page through the context processor listed
    in settings.py"""
    onboard_profile_data = request.session.get('onboard_profile_data',
                                               {
                                                    
                                               })
    context = {
        'onboard_profile_data': onboard_profile_data
    }
    return context
