from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, FarmProfile, FarmType
from customAuth.models import CustomUser


# Create your views here.
@login_required
def profile(request):
    user = request.user
    profile = get_object_or_404(CustomUser, email=request.user)
    print("user = ", profile)
    context = {
        'profile': profile,
    }
    return render(request, 'profiles/onboard_1.html', context)
