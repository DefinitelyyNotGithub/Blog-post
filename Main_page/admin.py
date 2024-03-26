from django.contrib import admin
from .models import (
    ContactUsModel,
    AboutUs_Model,
    site_general_info,

)


@admin.register(ContactUsModel)
class customedContactus(admin.ModelAdmin):
    list_filter = ['seen', 'date']
    list_display = ['subject', 'date', 'seen']


admin.site.register(site_general_info)
admin.site.register(AboutUs_Model)
