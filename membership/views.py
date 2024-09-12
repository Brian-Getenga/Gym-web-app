from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import MembershipForm
from .models import Membership

def create_membership(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            # Check if the user already has a membership
            existing_membership = Membership.objects.filter(user=request.user).first()
            if existing_membership:
                # Update existing membership if needed
                existing_membership.membership_type = form.cleaned_data['membership_type']
                existing_membership.start_date = form.cleaned_data['start_date']
                existing_membership.end_date = form.cleaned_data['end_date']
                existing_membership.save()
                messages.success(request, "Membership updated successfully.")
            else:
                # Create a new membership
                membership = form.save(commit=False)
                membership.user = request.user  # Set the user to the current logged-in user
                membership.save()
                messages.success(request, "Membership created successfully.")
            
            return redirect('membership_detail')  # Adjust the redirect URL as needed
    else:
        form = MembershipForm()

    return render(request, 'membership/create.html', {'form': form})



def membership_detail(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Adjust the redirect URL as needed

    # Get or create the membership for the user
    membership = get_object_or_404(Membership, user=request.user)

    return render(request, 'membership/membership_detail.html', {'membership': membership})
