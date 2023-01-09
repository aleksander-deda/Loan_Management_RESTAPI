from django.contrib import admin
from partners.models import Customer, Partner, PartnerProduct, LoanConfig


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = [ 'id', 
                    'name', 
                    'mobile', 
                    'nipt', 
                    'member',
                    'activity',
                    'bank',
                    'city',
                    'accountNumber',
                    
                    ]


@admin.register(PartnerProduct)
class PartnerProductAdmin(admin.ModelAdmin):
    list_display = ['id', 
                    'partner', 
                    'product',
                    'startDate', 
                    'endDate',
                    'isAssigned',
                    'isExpired',
                    'isActive', 
                    'isDeleted', 
                    'createdDate', 
                    'updatedDate'
                    
                    
                    ]



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 
                    'partner',
                    'firstName', 
                    'lastName', 
                    'personalId', 
                    'city',
                    'email',
                    'mobile', 
                    'gender', 
                    'idCardDoc',
                    'clausoleDoc', 
                    'birthdate', 
                    ]


@admin.register(LoanConfig)
class LoanConfig(admin.ModelAdmin):
    list_display = [
        'id', 
        'product',
        'minLoanTerm',
        'maxLoanTerm',
        'customerInterest',
        'applicationCommission',
        'bonus',
        ]