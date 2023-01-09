from rest_framework import serializers
from rest_framework.response import Response
from django.db import transaction, IntegrityError
import random, string
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



def generate_random_password(length):
    str = "".join(random.choice(string.ascii_letters) for i in range(length))
    return str



class ValidateUserDatas():
    
    def validateAmUwDatas(data):
            print('validating helpers...')

            name = data.get('name', None)
            if name is None:
                raise serializers.ValidationError("Emri nuk mund te jete bosh") 
            else:
                data['name']=name.lower().capitalize()


            surname = data.get('surname', None)
            if surname is None:
                raise serializers.ValidationError("Mbiemri nuk mund te jete bosh")
            else:
                data['surname']=surname.lower().capitalize()


            username = data.get('username', None)
            if username is None:
                raise serializers.ValidationError("Username nuk mund te jete bosh")


            email = data.get('email', None)
            if email is None:
                raise serializers.ValidationError("Email nuk mund te jete bosh")


            password = data.get('password', None)
            if password is None:
                raise serializers.ValidationError("Fjalekalimi nuk mund te jete bosh")


            mobile = data.get('mobile', None)
            if mobile is None:
                raise serializers.ValidationError("Numri i celularit nuk mund te jete bosh")
            print('validating ended succesfully')        

            return True
    
    
    def validatePartnerDatas(self, data):
        if self.partial:
            print('partial True')
            pass
        else:
            print('validating...')
    
            firstName = data.get('name', None)
            if firstName is None:
                raise serializers.ValidationError("Emri nuk mund te jete bosh") 
            else:
                data['name']=firstName.lower().capitalize()


            lastName = data.get('lastName', None)
            if lastName is None:
                raise serializers.ValidationError("Mbiemri nuk mund te jete bosh")
            else:
                data['lastName']=lastName.lower().capitalize()


            username = data.get('username', None)
            if username is None:
                raise serializers.ValidationError("Username nuk mund te jete bosh")


            email = data.get('email', None)
            if email is None:
                raise serializers.ValidationError("Email nuk mund te jete bosh")


            password = data.get('password', None)
            if password is None:
                raise serializers.ValidationError("Fjalekalimi nuk mund te jete bosh")


            mobile = data.get('mobile', None)
            if mobile is None:
                raise serializers.ValidationError("Numri i celularit nuk mund te jete bosh")


            personalId = data.get('personalId', None)
            if personalId is None:
                raise serializers.ValidationError("Numri Personal nuk mund te jete bosh")


            nipt = data.get('nipt', None)
            if nipt is None:
                raise serializers.ValidationError("Nipti nuk mund te jete bosh")

            accountNumber = data.get('accountNumber', None)
            if accountNumber is None:
                raise serializers.ValidationError("Numri i Llogarise nuk mund te jete bosh")

            bank = data.get('bank', None)
            if bank is None:
                raise serializers.ValidationError("Banka nuk mund te jete bosh")

            city = data.get('city', None)
            if city is None:
                raise serializers.ValidationError("Qyteti nuk mund te jete bosh")
            
            activity = data.get('activity', None)
            if activity is None:
                raise serializers.ValidationError("Aktiviteti nuk mund te jete bosh")
        
            print('validating ended succesfully')
        
        return True