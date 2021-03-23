from django.contrib import admin
from .models import service,serviceItem,galleryItem
from django.utils.html import mark_safe


admin.site.register(service)
admin.site.register(serviceItem)

admin.site.site_header = "Gowjee Admin"
admin.site.site_title = "Gowjee Admin Portal"
admin.site.index_title = "Welcome to Gowjee Admin Portal"

admin.site.register(galleryItem)
