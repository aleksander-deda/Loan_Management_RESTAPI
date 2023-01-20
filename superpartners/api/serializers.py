from rest_framework import serializers
from rest_framework.response import Response
from backoffice.api.serializers import MemberSerializer, CitySerializerGet
from backoffice.models import Product, Member, MemberType, Bank, City
from superpartners.models import SuperPartner
from django.db import transaction, IntegrityError
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from core.helpers.views_helpers.validate_datas import ValidateUserDatas, generate_random_password


class SuperPartnerSerializerGET(serializers.ModelSerializer):
    member = MemberSerializer(many=False, read_only=True)
    city = CitySerializerGet(many=False, read_only=True)
    
    class Meta:
        model=SuperPartner
        fields = "__all__"



class SuperPartnerSerializerPOST(serializers.ModelSerializer):
    member = MemberSerializer(many=False, read_only=True)
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.filter(isActive=True))
    username = serializers.CharField(max_length=150,required=False)
    email = serializers.EmailField(max_length=150, required=False)
    lastName = serializers.CharField(max_length=150, required=False)
    password = serializers.CharField(max_length=150., required=False)
    
    class Meta:
        model=SuperPartner
        fields = ['id','createdDate','name', 'code', 'member','city', 'nipt', 'mobile', 'activity', 'username', 
                  'email', 'lastName', 'password','isActive', 'isConfirmed', 'isDeleted']
       
        
    def validate(self, data):
        if self.partial:
            print('partial True')
            pass
        else:
            validated_datas = ValidateUserDatas.validateSuperPartnerDatas(self,data=data)
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
                    memberType=get_object_or_404(MemberType, code='super_partner'),
                    username=validatedData.get('username'),
                    user=user,
                    tmpPass=generate_random_password(8),
                )
                member.save()
                superPartnerCreated = SuperPartner.objects.create(
                    member = member,
                    name = validatedData.get('name'),
                    nipt = validatedData.get('nipt'),
                    code = validatedData.get('code'),
                    mobile = validatedData.get('mobile'),
                    city = validatedData.get('city'),
                    activity = validatedData.get('activity'),
                    
                )
                superPartnerCreated.save()
        
        except IntegrityError:
            return Response({'Something went wrong!!!'})
        print('created!!!')
        
        return superPartnerCreated
    
    
    def update(self, instance, validatedData):
        print('updating')
        datas ={
                'isActive' : validatedData.get('isActive', instance.isActive),
                'isDeleted' : validatedData.get('isDeleted', instance.isDeleted),
                'nipt' : validatedData.get('nipt', instance.nipt),
                 }
        instance.jsonDatas = datas
        instance.isUpdated = 'Pending'
        instance.save()
        print('updated')
        
        return instance