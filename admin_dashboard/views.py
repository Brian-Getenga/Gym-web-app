from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count, Sum
from membership.models import Membership
from store.models import Order
from blog.models import BlogPost
from events.models import Event
from django.utils import timezone


def is_staff(user):
    return user.is_staff

@user_passes_test(is_staff)
def admin_dashboard(request):
    total_members = Membership.objects.count()
    total_orders = Order.objects.count()
    total_revenue = Order.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0
    total_blog_posts = BlogPost.objects.count()
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).count()

    context = {
        'total_members': total_members,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'total_blog_posts': total_blog_posts,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'admin_dashboard/admin_dashboard.html', context)
