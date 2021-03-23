from django.shortcuts import render
from .models import service,serviceItem,galleryItem

def index(request):
    return render(request,"website/index.html",{
        "services":service.objects.all(),
        "galleryItems":galleryItem.objects.all()[:8]
    })

def about(request):
    return render(request,"website/about.html",{
        "services":service.objects.all()
    })

def services(request,id):
    return render(request,"website/service.html",{
        "services":service.objects.all(),
        "service":service.objects.get(id=id),
        "features":serviceItem.objects.filter(service__id=id)
    })

def contact(request):
    return render(request,"website/contact.html",{
        "services":service.objects.all()
    })

def gallery(request):
    return render(request,"website/gallery.html",{
        "services":service.objects.all(),
        "galleryItems":galleryItem.objects.all()
    })