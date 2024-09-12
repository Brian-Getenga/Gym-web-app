from django.shortcuts import render
from .models import Instructor

def about(request):
    instructors = Instructor.objects.all()
    return render(request, 'about/about.html', {'instructors': instructors})
