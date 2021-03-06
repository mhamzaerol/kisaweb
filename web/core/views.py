from django.shortcuts import render, HttpResponse, redirect

from .models import CourseResources

# Create your views here.

def homepage(request):
    return redirect('election')


def course_resources(request):
    resources = CourseResources.objects.order_by('class_id')
    return render(request, 'core/course_resources.html', context={
        'resources': resources,
    })
