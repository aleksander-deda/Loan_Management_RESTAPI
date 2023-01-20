from rest_framework import serializers
from rest_framework.response import Response
from ..models import LoanConfig, Partner
from backoffice.api.serializers import ProductSerializerGET, MemberSerializer, BankSerializerGet, CitySerializerGet
from backoffice.models import Product, Member, MemberType, Bank, City
from superpartners.models import SuperPartner
from django.db import transaction, IntegrityError
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from core.helpers.views_helpers.validate_datas import ValidateUserDatas, generate_random_password
import json
from rest_framework.decorators import action

RATING = (('A', 'A'), 
          ('B', 'B'),
          ('C', 'C'),
        )


class PartnerSerializerGET(serializers.ModelSerializer):
    
    member = MemberSerializer(many=False, read_only=True)
    city = CitySerializerGet(many=False, read_only=True)
    bank = BankSerializerGet(many=False, read_only=True)
    
    class Meta:
        model=Partner
        fields = "__all__"




class PartnerSerializerPOST(serializers.ModelSerializer):
    bank = serializers.PrimaryKeyRelatedField(queryset=Bank.objects.filter(isActive=True))
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.filter(isActive=True))
    superPartner = serializers.PrimaryKeyRelatedField(queryset=SuperPartner.objects.filter(isActive=True,isConfirmed=True), required=False)
    username = serializers.CharField(max_length=150,required=False)
    email = serializers.EmailField(max_length=150, required=False)
    lastName = serializers.CharField(max_length=150, required=False)
    password = serializers.CharField(max_length=150., required=False)
    member = MemberSerializer(many=False, read_only=True)   
    
    
    class Meta:
        model = Partner
        fields = ['id', 'createdDate', 'name', 'member','lastName', 'username', 'email', 'password', 'nipt', 'personalId', 'city', 'bank', 'mobile', 
                  'accountNumber', 'activity', 'isReferral', 'rating', 'superPartner', 'isActive', 'isConfirmed','isDeleted']
    
    
    def validate(self, data):
        if self.partial:
            print('partial True')
            pass
        else:
            validated_datas = ValidateUserDatas.validatePartnerDatas(self,data=data)
            if validated_datas==True:
                print('True')
                return data
        
        return data
    
    
    def create(self, validatedData,*args,**kwargs):
        print('creating...')
        
        try:
            with transaction.atomic():
                
                user = User.objects.create(
                    username=validatedData.get('username'),
                    first_name=validatedData.get('name'),
                    last_name=validatedData.get('lastName'),
                    email=validatedData.get('email')
                )
                user.set_password(validatedData.get('password'))
                user.save()
                member = Member.objects.create(
                    memberType=get_object_or_404(MemberType, code='partner'),
                    username=validatedData.get('username'),
                    user=user,
                    tmpPass=generate_random_password(8),
                )
                member.save()
                partnerCreated = Partner.objects.create(
                    member = member,
                    name = validatedData.get('name'),
                    personalId = validatedData.get('personalId'),
                    nipt = validatedData.get('nipt'),
                    mobile = validatedData.get('mobile'),
                    isReferral = validatedData.get('isReferral'),
                    rating = validatedData.get('rating', None),
                    accountNumber = validatedData.get('accountNumber'),
                    superPartner = validatedData.get('superPartner', None),
                    bank = validatedData.get('bank'),
                    city = validatedData.get('city'),
                    activity = validatedData.get('activity'),
                    
                )
                partnerCreated.save()
        
        except IntegrityError:
            return Response({'Something went wrong!!!'})
        print('created!!!')
        
        return partnerCreated
    
    
    def update(self, instance, validatedData):
        print('updating')
        datas ={
                'isActive' : validatedData.get('isActive', instance.isActive),
                'personalId': validatedData.get('personalId', instance.personalId),
                'nipt' : validatedData.get('nipt', instance.nipt),
                'isReferral': validatedData.get('isReferral', instance.isReferral),
                'rating': validatedData.get('rating', instance.rating),
                'bank': str(validatedData.get('bank', instance.bank).id),
                'accountNumber': validatedData.get('accountNumber',instance.accountNumber),
                 
                 }
        instance.jsonDatas = datas
        instance.isUpdated = 'Pending'
        instance.save()
        print('updated')
        
        return instance

   
    



class LoanConfigSerializerGET(serializers.ModelSerializer):
    
    product = ProductSerializerGET(many=False, read_only=True)
    
    class Meta:
        model = LoanConfig
        fields = ['id', 'product', 'minLoanTerm', 'maxLoanTerm', 'customerInterest', 'applicationCommission','isActive' ]
      
      
      
 
class LoanConfigSerializerPOST(serializers.ModelSerializer):
    
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    
    class Meta:
        model = LoanConfig
        fields = "__all__"
    
    
    def validate(self, data):
        if self.partial:
            print('partial update')
            pass
        else:
            print('validating...')
            minLoanTerm = data.get('minLoanTerm', None)
            if minLoanTerm is None:
                raise serializers.ValidationError("Kohezgjatja minimale nuk mund te jete bosh") 
            
            maxLoanTerm = data.get('maxLoanTerm', None)
            if maxLoanTerm is None:
                raise serializers.ValidationError("Kohezgjatja maksimale nuk mund te jete bosh")
            
            applicationCommission = data.get('applicationCommission', None)
            if applicationCommission is None:
                raise serializers.ValidationError("Komisioni i aplikimit nuk mund te jete bosh")
            
            customerInterest = data.get('customerInterest', None)
            if customerInterest is None:
                raise serializers.ValidationError("Interesi i klientit nuk mund te jete bosh")

        return data
    


    def update(self, instance, validatedData):
        print('worlddddd')
        instance.minLoanTerm = validatedData.get('minLoanTerm', instance.minLoanTerm)
        instance.maxLoanTerm = validatedData.get('maxLoanTerm', instance.maxLoanTerm)
        instance.customerInterest = validatedData.get('customerInterest', instance.customerInterest)
        instance.applicationCommission = validatedData.get('applicationCommission', instance.applicationCommission)
        instance.bonus = validatedData.get('bonus', instance.bonus)
        instance.isActive = validatedData.get('isActive', instance.isActive)
        instance.save()
        
        return instance