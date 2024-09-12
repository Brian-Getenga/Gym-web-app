from django.shortcuts import render
from .models import Class

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'classes_programs/class_list.html', {'classes': classes})