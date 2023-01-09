from django.db import models
from django.db.models.deletion import CASCADE
from .validators import validate_file_extension
from superpartners.models import SuperPartner


RATING = (('A', 'A'), 
          ('B', 'B'),
          ('C', 'C'),
        )

GENDER = (('M', 'M'),
          ('F', 'F'),
        )
          

CITIES = (('BERAT', 'BERAT'), 
          ('BULQIZE', 'BULQIZE'),
          ('DELVINE', 'DELVINE'),
          ('DEVOLL', 'DEVOLL'),
          ('DIBER', 'DIBER'),
          ('DURRES', 'DURRES'),
          ('ELBASAN', 'ELBASAN'),
          ('FIER', 'FIER'),
          ('GJIROKASTER', 'GJIROKASTER'),
          ('GRAMSH', 'GRAMSH'),
          ('HAS', 'HAS'),
          ('KAVAJE', 'KAVAJE'),
          ('KOLONJE', 'KOLONJE'),
          ('KORCE', 'KORCE'),
          ('KRUJE', 'KRUJE'),
          ('SKRAPAR', 'SKRAPAR'),
          ('KUCOVE', 'KUCOVE'),
          ('KUKES', 'KUKES'),
          ('KURBIN', 'KURBIN'),
          ('LEZHE', 'LEZHE'),
          ('LIBRAZHD', 'LIBRAZHD'),
          ('LUSHNJE', 'LUSHNJE'),
          ('MALESI E MADHE', 'MALESI E MADHE'),
          ('MALLAKASTER', 'MALLAKASTER'),
          ('MAT', 'MAT'),
          ('MIRDITE', 'MIRDITE'),
          ('PEQIN', 'PEQIN'),
          ('PERMET', 'PERMET'),
          ('POGRADEC', 'POGRADEC'),
          ('PUKE', 'PUKE'),
          ('SARANDE', 'SARANDE'),
          ('SHKODER', 'SHKODER'),
          ('TEPELENE', 'TEPELENE'),
          ('TIRANE', 'TIRANE'),
          ('TROPOJE', 'TROPOJE'),
          ('VLORE', 'VLORE'),
        )


BANKS = (('BANKA RAIFFEISEN','BANKA RAIFFEISEN'),
         ('BANKA KOMBETARE TREGTARE (BKT)','BANKA KOMBETARE TREGTARE (BKT)'),
         ('BANKA TIRANA','BANKA TIRANA'),
         ('BANKA OTP','BANKA OTP'),
         ('BANKA INTESA SANPAOLO ALBANIA','BANKA INTESA SANPAOLO ALBANIA'),
         ('BANKA CREDINS','BANKA CREDINS'),
         ('BANKA NDERKOMBETARE TREGTARE','BANKA NDERKOMBETARE TREGTARE'),
         ('BANKA ALPHA ALBANIA','BANKA ALPHA ALBANIA'),
         ('BANKA PROCREDIT','BANKA PROCREDIT'),
         ('BANKA SOCIETE GENERALE ALBANIA','BANKA SOCIETE GENERALE ALBANIA'),
         ('BANKA UNION','BANKA UNION'),
         ('BANKA AMERICAN BANK OF INVESTMENTS (abi)','BANKA AMERICAN BANK OF INVESTMENTS (abi)'),
         )


class Partner(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    personalId = models.CharField(max_length=10, null=False, blank=False, unique=True)
    mobile = models.CharField(max_length=16, null=False, blank=False)
    nipt = models.CharField(max_length=13, null=False, blank=False, unique=True)
    member = models.ForeignKey('backoffice.Member', on_delete=models.CASCADE)
    isReferral = models.BooleanField(default=False)
    rating = models.CharField(choices= RATING, max_length=10, null=True, blank=True)
    city = models.ForeignKey('backoffice.City', on_delete=models.CASCADE)
    activity = models.CharField(max_length=500)
    bank = models.ForeignKey('backoffice.Bank', on_delete=models.CASCADE)
    accountNumber = models.CharField(max_length=30)
    jsonDatas = models.JSONField(null=True, blank=True)
    superPartner = models.ForeignKey(SuperPartner, on_delete=models.CASCADE, null=True, blank=True)
    isUpdated = models.CharField(max_length=20, null=True, blank=True, default="No")
    isConfirmed = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='partners'

    
    def __str__(self):
        return self.member.user.first_name + ' ' + self.member.user.last_name
    
    
    
    
class PartnerProduct(models.Model):
    partner = models.ForeignKey('partners.Partner', on_delete=models.CASCADE)
    product = models.ForeignKey('backoffice.Product', on_delete=models.CASCADE)
    startDate = models.DateField(null=False, blank=False)
    endDate = models.DateField(null=True, blank=True)
    jsonDatas = models.JSONField(null=True, blank=True)
    isUpdated = models.CharField(max_length=20, null=True, blank=True, default="No")
    isConfirmed = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedDate = models.DateTimeField(auto_now=True, blank=True, null=True)
    isAssigned = models.BooleanField(default=False)
    isExpired = models.BooleanField(default=False)
    
    class Meta:
        db_table='partner_products'


    def __str__(self):
        return self.partner.member.user.first_name + ' ' + self.partner.member.user.first_name + ' - ' + self.product.productName
    
    

    


class LoanConfig(models.Model):
    product = models.ForeignKey('backoffice.Product', on_delete=models.CASCADE)
    minLoanTerm = models.IntegerField()
    maxLoanTerm = models.IntegerField()
    customerInterest = models.FloatField(null=True, blank=True)
    applicationCommission = models.FloatField(null=True, blank=True)
    bonus = models.FloatField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table='loan_configs'


    def __str__(self):
        return self.product.productName + ' : ' + str(self.minLoanTerm) + ' - ' + str(self.maxLoanTerm)


class Customer(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=128, null=False, blank=False)
    lastName = models.CharField(max_length=128, null=False, blank=False)
    personalId = models.CharField(max_length=11, null=False, blank=False)
    city = models.ForeignKey('backoffice.City', on_delete=models.CASCADE)
    email = models.EmailField(max_length=250)
    idCardDoc = models.FileField(upload_to="file/id_cards/%Y/%m/%d/",validators=[validate_file_extension], null=False, blank=False)
    clausoleDoc = models.FileField(upload_to="file/clausoles/%Y/%m/%d/" ,validators=[validate_file_extension], null=False, blank=False)
    birthdate = models.DateField()
    gender = models.IntegerField(choices = GENDER)
    mobile = models.CharField(max_length=16)
    status = models.CharField(max_length=50, null=True, blank=True)
    consent_boa = models.CharField(max_length=10, null=True, blank=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=True)
    
    
    class Meta:
        db_table='customers'

    
    def __str__(self):
        return self.firstName + ' ' + self.lastName


