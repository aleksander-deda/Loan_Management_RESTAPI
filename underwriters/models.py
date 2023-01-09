from django.db import models
from django.db.models.deletion import CASCADE
from backoffice.models import Member



class UnderWriter(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='underwriters'

    
    def __str__(self):
        return self.member.user.first_name + ' ' + self.member.user.last_name