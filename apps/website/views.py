from django.shortcuts import render

def index(request):
    
    context = {
    }
    
    return render(request, 'website/index.html', context)

def enrol(request):
    
    context = {
    }
    
    return render(request, 'website/enrol.html', context)

def courses(request):
    
    context = {
    }
    
    return render(request, 'website/courses.html', context)
