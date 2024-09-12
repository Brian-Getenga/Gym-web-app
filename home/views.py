""" from django.shortcuts import render
from .models import Announcement

def home(request):
    announcements = Announcement.objects.order_by('-date_posted')[:5]
    return render(request, 'home/index.html', {'announcements': announcements})
 """

from django.shortcuts import render
from .models import Announcement,Plan, Testimonial, Statistic, AboutUs
from classes_programs.models import Class
from about.models import Instructor

def home(request):
    announcements = Announcement.objects.order_by('-date_posted')[:5]
    classes = Class.objects.all()[:3]
    plans = Plan.objects.all()
    testimonials = Testimonial.objects.all()
    statistics = Statistic.objects.all()
    about_us = AboutUs.objects.first()
    instructors = Instructor.objects.all()



    return render(request, 'home/index.html', {
        'announcements': announcements,
        'classes': classes,
        'plans': plans,
        'testimonials': testimonials,
        'statistics' : statistics,
        'about_us': about_us,
        'instructors':  instructors
    })




