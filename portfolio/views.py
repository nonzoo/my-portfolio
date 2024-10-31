from django.shortcuts import render
from .models import Project,Frontend,Backend


def homeview(request):
    projects = Project.objects.all()
    frontends = Frontend.objects.all()
    backends= Backend.objects.all()

    
    print(frontends)
    return render (request, 'portfolio/home.html',  {
        'projects':projects,
        'frontends':frontends,
        'backends': backends
    })


