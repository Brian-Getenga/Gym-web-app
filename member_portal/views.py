from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MemberProfile, Achievement
from .forms import MemberProfileForm

@login_required
def member_dashboard(request):
    try:
        profile = request.user.memberprofile
    except MemberProfile.DoesNotExist:
        profile = MemberProfile.objects.create(user=request.user)
    
    achievements = Achievement.objects.filter(user=request.user)
    return render(request, 'member_portal/member_dashboard.html', {'profile': profile, 'achievements': achievements})

@login_required
def edit_profile(request):
    profile, created = MemberProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = MemberProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('member_dashboard')
    else:
        form = MemberProfileForm(instance=profile)
    return render(request, 'member_portal/edit_profile.html', {'form': form})