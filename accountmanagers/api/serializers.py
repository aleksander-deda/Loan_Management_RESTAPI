from rest_framework import serializers
from rest_framework.response import Response
from ..models import AccountManager
from backoffice.api.serializers import MemberSerializer
from backoffice.models import Member, MemberType
from django.db import transaction, IntegrityError
import random, string
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from core.helpers.views_helpers.validate_datas import generate_random_password, ValidateUserDatas




class AccountManagerSerializerGET(serializers.ModelSerializer):
    
    member = MemberSerializer(many=False, read_only=True)
    
    class Meta:
        model=AccountManager
        fields = ['id', 'name', 'member', 'code', 'mobile', 'isActive', 'createdDate', 'updatedDate', 'isDeleted']




class AccountManagerSerializerPOST(serializers.ModelSerializer):
    member = MemberSerializer(many=False, read_only=True)
    username = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(max_length=150, required=False)
    lastName = serializers.CharField(max_length=150, required=False)
    password = serializers.CharField(max_length=150, required=False)   
    
    class Meta:
        model = AccountManager
        fields = ['id','name', 'member','code', 'username','email','lastName','password', 'mobile', 'isActive', 'isDeleted']
        
    
    
    def validate(self, data):
        if self.partial:
            print('partial True')
            pass
        else:
            validated_datas = ValidateUserDatas.validateAmUwDatas(data=data)
            if validated_datas==True:
                print('True')
                return data
        
        return data
       
    
    
    def create(self, validatedData):
        print('creating...')
        
        try:
            with transaction.atomic():
                username = validatedData['username']
                email = validatedData['email']
                password = validatedData['password']
                firstName = validatedData['name']
                lastName = validatedData['lastName']
                mobile = validatedData['mobile']
                code = validatedData['code']
                
                user = User.objects.create(
                    username=username,
                    first_name=firstName,
                    last_name=lastName,
                    email=email
                )
                user.set_password(password)
                user.save()
                member = Member.objects.create(
                    memberType=get_object_or_404(MemberType, code='account_manager'),
                    username=username,
                    user=user,
                    tmpPass=generate_random_password(8),
                )
                member.save()
                amCreated = AccountManager.objects.create(
                    member=member,
                    mobile=mobile,
                    name=firstName,
                    code=code
                )
                amCreated.save()
        
        except IntegrityError as err:
            return Response({'Something went wrong!!!'})
        print('created!!!')    
        return amCreated
    
    
    
    def update(self, instance, validatedData):
        print('updating')
        instance.isActive = validatedData.get('isActive', instance.isActive)
        instance.isDeleted = validatedData.get('isDeleted', instance.isDeleted)
        instance.save()
        print('updated')
        
        return instance