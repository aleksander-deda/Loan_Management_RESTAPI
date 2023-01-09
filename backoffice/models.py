from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from partners.validators import validate_file_extension
from partners.models import Customer, Partner, PartnerProduct



CURRENCY = (('ALL', 'ALL'), 
            ('EURO', 'EURO'))




class Product(models.Model):
    productName = models.CharField(max_length= 100, null=False, blank=False)
    code = models.CharField(max_length=30, unique=True, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    minValue = models.FloatField(null=False, blank=False)
    maxValue = models.FloatField(null=False, blank=False)
    term = models.IntegerField(null=False, blank=False)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='products'

    def __str__(self):
        return self.productName



class Prelead(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    partnerProduct = models.ForeignKey(PartnerProduct, on_delete=models.CASCADE)
    appliedAmount = models.DecimalField(max_digits= 10, decimal_places=2, null=False, blank=False)
    approvedAmount = models.DecimalField(max_digits= 10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(choices= CURRENCY, max_length=10, null=True, blank=True, default="ALL")
    loanTerm = models.IntegerField(null=True, blank=True)
    monthlyLoan = models.DecimalField(max_digits= 10, decimal_places=2)
    partnerContract = models.FileField(upload_to="files/partner_contracts/%Y/%m/%d/",validators=[validate_file_extension], null=True, blank=True)
    uwContract = models.FileField(upload_to="files/uw_contracts/%Y/%m/%d/",validators=[validate_file_extension], null=True, blank=True)
    doc_1 = models.FileField(upload_to="files/additional_docs/%Y/%m/%d/",validators=[validate_file_extension], null=True, blank=True)
    doc_2 = models.FileField(upload_to="files/additional_docs/%Y/%m/%d/",validators=[validate_file_extension], null=True, blank=True)
    sellerName = models.CharField(max_length=60, null=False, blank=False)
    sellerPhone = models.CharField(max_length=16, null=False, blank=False)
    applicationStatus = models.CharField(null=True, blank=True, max_length=20, default="Pending")
    rejectionReason = models.CharField(max_length=500, null=True, blank=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedDate = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table='preleads'

    def __str__(self):
        return self.customer.first_name  + ' ' + self.customer.last_name + ' - ' + self.partnerProduct.product.productName 
    
    
    
class MemberType(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=250, null=False, blank=False)
    code = models.CharField(max_length=80, unique=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table='member_types'

    def __str__(self):
        return self.name



class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    username = models.CharField(max_length=200, unique=True)
    memberType = models.ForeignKey(MemberType, on_delete=models.CASCADE, related_name='memberType')
    tmpPass = models.CharField(max_length=200, null=False, blank=False)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        db_table='members'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    
class ActionType(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=500, unique=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        db_table = 'action_types'
        
    def __str__(self):
        return self.name


class Audit(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    memberType = models.CharField(max_length=200)
    actionType = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    createdProduct = models.CharField(max_length=200, blank=True, null=True)
    createdAm = models.CharField(max_length=200, blank=True, null=True)
    createdUw = models.CharField(max_length=200, blank=True, null=True)
    createdPartner = models.CharField(max_length=200, blank=True, null=True)
    createdSuperPartner = models.CharField(max_length=200, blank=True, null=True)
    createdLoanconfig = models.CharField(max_length=200, blank=True, null=True)
    affectedAm = models.CharField(max_length=200, blank=True, null=True)
    affectedUw = models.CharField(max_length=200, blank=True, null=True)
    affectedProduct = models.CharField(max_length=200, blank=True, null=True)
    affectedPartner = models.CharField(max_length=200, blank=True, null=True)
    affectedSuper_partner = models.CharField(max_length=200, blank=True, null=True)
    affectedCustomer = models.CharField(max_length=200, blank=True, null=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'audit'
        
    def __str__(self):
        return self.member.user.first_name + ' ' + self.member.user.last_name + ' - ' + self.member.memberType.name + ' : ' + self.action_type.code
    
 
class MemberLogin(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    memberType = models.CharField(max_length=200)
    ipAddress = models.CharField(max_length=200, blank=True, null=True)
    actionType = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    loggedIn = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'member_logins'
        
    def __str__(self):
        return self.member.user.first_name + ' ' + self.member.user.last_name + ' - ' + self.member.member_type.name 
    
    
class City(models.Model):
    name = models.CharField(max_length=255)
    cityCode = models.IntegerField(unique=True)
    country = models.CharField(max_length=255, default="Albania")
    isActive = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
        
    class Meta:
        db_table = 'cities'
    
    def __str__(self):
        return self.name + ' - ' + str(self.cityCode)
        
        
    
class Bank(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    isActive = models.BooleanField(default=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'banks'
        
    def __str__(self):
        return self.name + ' - ' + str(self.code)
    





