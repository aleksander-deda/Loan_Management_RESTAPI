from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
# from backoffice.models import Member


class SuperPartner(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    member = models.ForeignKey('backoffice.Member', on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True, null=False, blank=False)
    city = models.ForeignKey('backoffice.City', on_delete=models.CASCADE)
    nipt = models.CharField(max_length=10, unique=True)
    activity = models.CharField(max_length=30, null=False, blank=False)
    mobile = models.IntegerField(null=False, blank=False)
    jsonDatas = models.JSONField(null=True, blank=True)
    isUpdated = models.CharField(max_length=20, null=True, blank=True, default="No")
    isConfirmed = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedDate = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table='superpartners'

    
    def __str__(self):
        return self.member.user.first_name + ' ' + self.member.user.last_name





