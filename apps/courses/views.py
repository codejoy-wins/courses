# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import Course

def index(request):
    print "index"
    context = {
        "jay": "silent bob",
        "courses": Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    print "adding"
    print request.POST['name']
    Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/')

def destroy(request, course_id):
    print "destroying"
    print course_id
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/')

def confirm(request, course_id):
    print "confirming"
    print course_id
    context = {
        'course' : Course.objects.get(id=course_id)
    }
    return render(request, 'courses/confirm.html', context)

def odell(request):
    return HttpResponse("odell catches everything")