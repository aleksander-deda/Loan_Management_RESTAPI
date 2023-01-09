from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth.models import User
from .. models import Member, MemberType, City, Bank, Product



class ProductSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class ProductSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    
    def validate(self, data):
        if self.partial:
            print('partial update')
            pass
        else:
            print('validating...')
            productName = data.get('productName', None)
            if productName is None:
                raise serializers.ValidationError("Emri i Produktit nuk mund te jete bosh") 
            
            code = data.get('code', None)
            if code is None:
                raise serializers.ValidationError("Kodi nuk mund te jete bosh")
            
            description = data.get('description', None)
            if description is None:
                raise serializers.ValidationError("Pershkrimi nuk mund te jete bosh")
            
            minValue = data.get('minValue', None)
            if minValue is None:
                raise serializers.ValidationError("Vlera minimale nuk mund te jete bosh")
            
            maxValue = data.get('maxValue', None)
            if maxValue is None:
                raise serializers.ValidationError("Vlera maksimale nuk mund te jete bosh")
            
            term = data.get('term', None)
            if term is None:
                raise serializers.ValidationError("Kohezgjatja nuk mund te jete bosh")

        return data
    

    def update(self, instance, validatedData):
        print('worlddddd')
        instance.productName = validatedData.get('productName', instance.productName)
        instance.minValue = validatedData.get('minValue',instance.minValue)
        instance.maxValue = validatedData.get('maxValue',instance.maxValue)
        instance.term = validatedData.get('term',instance.term)
        instance.isActive = validatedData.get('isActive', instance.isActive)
        instance.save()
        
        return instance





class CitySerializerGet(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','name', 'cityCode', 'country', 'isActive', 'createdDate']
      
      
      
 
class CitySerializerPost(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'cityCode', 'country', 'isActive']
    
    
    def validate(self, data):
        if self.partial:
            print('partial update')
            pass
        else:
            print('validating...')
            name = data.get('name', None)
            if name is None:
                raise serializers.ValidationError("Emertimi i emrit nuk mund te jete bosh") 
            else:
                data['name'] = name.upper()
            
            cityCode = data.get('cityCode', None)
            if cityCode is None:
                raise serializers.ValidationError("Kodi nuk mund te jete bosh")
            
            if City.objects.filter(cityCode__contains=data['cityCode']).exists():
                raise serializers.ValidationError({'Info': f'Qyteti me kodin {data["cityCode"]} ekziston tashme!'})

        return data
    

    def update(self, instance, validatedData):
        print('worlddddd')
        instance.name = validatedData.get('name', instance.name).upper()
        instance.isActive = validatedData.get('isActive', instance.isActive)
        instance.cityCode = validatedData.get('cityCode', instance.cityCode)
        instance.save()
        
        return instance
    
      
        
        
class BankSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id','name', 'code', 'isActive', 'createdDate']




class BankSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id' ,'name', 'code', 'isActive']

    def validate(self, data):
        if self.partial:
            pass
        else:
            name = data.get('name', None).lower().upper()
            if name is None:
                raise serializers.ValidationError("Emertimi i emrit nuk mund te jete bosh") 
            else:
                data["name"]=name
            
            code = data.get('code', None).lower().upper()
            if code is None:
                raise serializers.ValidationError("Kodi nuk mund te jete bosh")
            else:
                data["code"]=code

        return data

    def update(self, instance, validatedData):
        print('worlddddd')
        instance.name = validatedData.get('name', instance.name)
        instance.isActive = validatedData.get('isActive', instance.isActive)
        instance.code = validatedData.get('code', instance.code)
        instance.save()
        
        return instance
    
    


class MemberTypeSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = MemberType
        fields = ['id','name', 'description','code', 'isActive', 'createdDate']




class MemberTypeSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = MemberType
        fields = ['id','name', 'description', 'code', 'isActive']
        
    def validate(self, data):
        if self.partial:
            pass
        else:
            name = data.get('name', None)
            if name is None:
                raise serializers.ValidationError("Emri nuk mund te jete bosh") 

            description = data.get('description', None)
            if description is None:
                raise serializers.ValidationError("Pershkrimi nuk mund te jete bosh")

            code = data.get('code', None).lower()
            if code is None:
                raise serializers.ValidationError("Kodi nuk mund te jete bosh")
            else:
                data["code"]=code
                
        return data
        
    
    def update(self, instance, validatedData):
        print('worlddddd')
        instance.name = validatedData.get('name', instance.name)
        instance.description = validatedData.get('description', instance.description)
        instance.isActive = validatedData.get('isActive', instance.isActive)
        instance.save()
        
        return instance




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',"username", "first_name", "last_name", "email", "password", "last_login"]
        extra_kwargs = {
            'password': {'write_only': True}
        }



class MemberSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    memberType = MemberTypeSerializerPost(many=False, read_only=True)
    
    class Meta:
        model = Member
        fields = ['id','user', 'memberType', 'tmpPass','username', 'isActive', 'isDeleted', 'createdDate']








# class MemberTypeSerializerPost(serializers.ModelSerializer):
#     class Meta:
#         model = MemberType
#         fields = ['id']

    

