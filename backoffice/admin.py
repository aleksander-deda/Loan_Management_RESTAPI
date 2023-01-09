from django.contrib import admin


from .models import Member, MemberType, Product, Prelead, ActionType, Audit, MemberLogin, Bank, City


@admin.register(MemberType)
class MemberTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 
                    'description', 
                    'code'
                    ]



@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 
                    'username', 
                    'memberType', 
                    'tmpPass'
                    ]
    
    
@admin.register(Prelead)
class PreleadAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'partnerProduct',
        'appliedAmount',
        'approvedAmount',
        'currency',
        'loanTerm',
        'monthlyLoan',
        'partnerContract',
        'uwContract',
        'doc_1',
        'doc_2',
        'sellerName',
        'sellerPhone',
        'applicationStatus',
        'rejectionReason',
        'createdDate',
    ]
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
                    'productName',
                    'code',
                    'description',
                    'minValue',
                    'maxValue',
                    'term',   
                    ]


@admin.register(ActionType)
class ActionTypeAdmin(admin.ModelAdmin):
    list_display = [
                    'name',
                    'code',
                    'isActive',
                    'isDeleted',
                    'createdDate',
                    'updatedDate',
                    ]


@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = [
                    'id',
                    'member',
                    'memberType',
                    'actionType',
                    'createdProduct',
                    'createdAm',
                    'createdUw',
                    'createdPartner',
                    'createdSuperPartner',
                    'createdLoanconfig',
                    'affectedPartner',
                    'affectedProduct',
                    'affectedCustomer',
                    'createdDate',
                    ]
    
    
@admin.register(MemberLogin)
class MemberLoginAdmin(admin.ModelAdmin):
    list_display = [
        'member',
        'memberType',
        'ipAddress',
        'actionType',
        'loggedIn',
    ]    


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'cityCode',
                    'country',
                    'isActive',
                    'createdDate',
                    'updatedDate',
                    ]


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'code',
                    'isActive',
                    'createdDate',
                    'updatedDate',
                    ]