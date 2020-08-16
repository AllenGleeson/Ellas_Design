from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    
    form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form
    }

    return render(request, template, context)