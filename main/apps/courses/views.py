from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import error
from django.contrib import messages
from models import *
from .models import Course

# Create your views here.
def index(request):
    context = {
        "course_data":Course.objects.all()
    }
    
    return render(request, 'courses/index.html', context)
def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    else:
        Course.objects.create(
            name = request.POST['name'],
            desc = request.POST['desc']
            )
    return redirect('/')

def caution(request, id):
    
    return render(request, 'courses/destroy.html', {"course":Course.objects.get(id = id)})

def destroy(request, id):
    destroy_data = Course.objects.get(id = id).delete()
    # destroy_data.delete()
    # destroy_data.save()
    
    return redirect('/')
    
