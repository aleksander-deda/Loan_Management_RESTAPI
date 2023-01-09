from django.contrib import admin
from .models import SuperPartner


@admin.register(SuperPartner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = [ 
                    'name',
                    'member',
                    'code',
                    'city',
                    'nipt',
                    'activity',
                    'mobile',
                    
                    ]
