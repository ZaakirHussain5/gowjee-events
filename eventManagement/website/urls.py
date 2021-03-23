from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('service/<id>',views.services,name="service"),
    path('gallery',views.gallery,name="gallery"),
    path('contact',views.contact,name="contact"),
]