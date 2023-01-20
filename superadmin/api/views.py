import backoffice.api.serializers as backofficeserializers
import partners.api.serializers as partnerserializers
from backoffice.models import Bank, City, MemberType, Product
from accountmanagers.models import AccountManager
from underwriters.models import UnderWriter
from partners.models import LoanConfig
from accountmanagers.api.serializers import AccountManagerSerializerPOST, AccountManagerSerializerGET
from underwriters.api.serializers import UnderwriterSerializerPOST, UnderwriterSerializerGET
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated




class AccountManagerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def queryset():
        queryset = AccountManager.objects.all()
        return queryset
    
    
    def list(self, request):
        queryset = AccountManagerViewSet.queryset()
        serializer = AccountManagerSerializerGET(queryset, many=True)
        return Response(serializer.data)
   
    
    def retrieve(self, request, pk):
        queryset = AccountManagerViewSet.queryset()
        am = get_object_or_404(queryset, pk=pk)
        serializer = AccountManagerSerializerGET(am, many=False)
        return Response(serializer.data)
    
    
    def create(self, request, pk=None):
        serializer = AccountManagerSerializerPOST(data=request.data, many=False)
        
        if User.objects.filter(username=request.data["username"]).exists():
            return Response({'Info': f'Perdoruesi me username {request.data["username"]} ekziston tashme!'})
        
        if AccountManager.objects.filter(code=request.data["code"]).exists():
            return Response({'Info': f'AM me kodin {request.data["code"]} ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()
        
        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per AM!!'})
        
        return Response(serializer.data)
        
        
    
    def update(self, request, pk):
        queryset = AccountManagerViewSet.queryset()
        am = get_object_or_404(queryset, pk=pk)
        serializer = AccountManagerSerializerPOST(instance=am, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikimin e AM !!'})
        return Response(serializer.data)
    
    
    
    
class UnderwriterViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    
    def queryset():
        queryset = UnderWriter.objects.all()
        return queryset
    
    
    def list(self, request):
        queryset = UnderwriterViewSet.queryset()
        serializer = UnderwriterSerializerGET(queryset, many=True)
        return Response(serializer.data)
   
    
    def retrieve(self, request, pk):
        queryset = UnderwriterViewSet.queryset()
        uw = get_object_or_404(queryset, pk=pk)
        serializer = UnderwriterSerializerGET(uw, many=False)
        return Response(serializer.data)
    
    

    def create(self, request, pk=None):
        serializer = UnderwriterSerializerPOST(data=request.data, many=False)
        
        if User.objects.filter(username=request.data["username"]).exists():
            return Response({'Info': f'Perdoruesi me username {request.data["username"]} ekziston tashme!'})
        
        if UnderWriter.objects.filter(code=request.data["code"]).exists():
            return Response({'Info': f'UW me kodin {request.data["code"]} ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()
        
        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per UW!!'})
        
        return Response(serializer.data)
        
        
    
    def update(self, request, pk):
        queryset = UnderwriterViewSet.queryset()
        uw = get_object_or_404(queryset, pk=pk)
        serializer = UnderwriterSerializerPOST(instance=uw, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikimin e UW !!'})
        return Response(serializer.data)



class ProductViewSet(viewsets.ViewSet):
    
    def queryset():
        queryset = Product.objects.all()
        return queryset
    
    
    def list(self, request):
        queryset = ProductViewSet.queryset()
        serializer = backofficeserializers.ProductSerializerGET(queryset, many=True)
        return Response(serializer.data)
   
    
    def retrieve(self, request, pk):
        queryset = ProductViewSet.queryset()
        product = get_object_or_404(queryset, pk=pk)
        serializer = backofficeserializers.ProductSerializerGET(product, many=False)
        return Response(serializer.data)
    

    def create(self, request, pk=None):
        serializer = backofficeserializers.ProductSerializerPOST(data=request.data, many=False)
        
        if Product.objects.filter(code=request.data["code"]).exists():
            return Response({'Info': f'Produkti me kodin {request.data["code"]} ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()
        
        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per Produktin !!'})
        
        return Response(serializer.data)
        
        
    
    def update(self, request, pk):
        queryset = ProductViewSet.queryset()
        product = get_object_or_404(queryset, pk=pk)
        serializer = backofficeserializers.ProductSerializerPOST(instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikimin e Produktit !!'})
        return Response(serializer.data)



class LoanConfigViewSet(viewsets.ViewSet):
    
    def queryset():
        queryset = LoanConfig.objects.all()
        return queryset
    
    
    def list(self, request):
        queryset = LoanConfigViewSet.queryset()
        serializer = partnerserializers.LoanConfigSerializerGET(queryset, many=True)
        return Response(serializer.data)
   
    
    def retrieve(self, request, pk):
        queryset = LoanConfigViewSet.queryset()
        loanConfig = get_object_or_404(queryset, pk=pk)
        serializer = partnerserializers.LoanConfigSerializerGET(loanConfig, many=False)
        return Response(serializer.data)
    

    def create(self, request, pk=None):
        serializer = partnerserializers.LoanConfigSerializerPOST(data=request.data, many=False)
        
        if LoanConfig.objects.filter(product__id=request.data["product"], minLoanTerm=request.data["minLoanTerm"], maxLoanTerm=request.data["maxLoanTerm"]).exists():
            print('ekziston')
            return Response({'Info': f'Konfigurimi me keto te dhena per kete Produkt ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()
        
        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per Konfigurimin !!'})
        
        return Response(serializer.data)
        
        
    
    def update(self, request, pk):
        queryset = LoanConfigViewSet.queryset()
        product = get_object_or_404(queryset, pk=pk)
        serializer = partnerserializers.LoanConfigSerializerPOST(instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikimin e Produktit !!'})
        return Response(serializer.data)



class CityViewSet(viewsets.ViewSet):
    
    def queryset():
        queryset = City.objects.all()
        return queryset
    
    
    def list(self, request):
        queryset = CityViewSet.queryset()
        serializer = backofficeserializers.CitySerializerGet(queryset, many=True)
        return Response(serializer.data)
   
    
    def retrieve(self, request, pk):
        queryset = CityViewSet.queryset()
        city = get_object_or_404(queryset, pk=pk)
        serializer = backofficeserializers.CitySerializerGet(city, many=False)
        return Response(serializer.data)
    
    
    def create(self, request, pk=None):
        serializer = backofficeserializers.CitySerializerPost(data=request.data, many=False)
        
        if City.objects.filter(cityCode__iexact=request.data['cityCode']).exists():
            return Response({'Info': f'Qyteti me kodin {request.data["cityCode"]} ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()
        
        else:
            return serializers.ValidationError({'Error': 'Nuk keni plotesuar sakte formen per qytetin!!'})
        
        return Response(serializer.data)
        
        
    
    def update(self, request, pk):
        queryset = CityViewSet.queryset()
        city = get_object_or_404(queryset, pk=pk)
        serializer = backofficeserializers.CitySerializerPost(instance=city, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikim!!'})
        return Response(serializer.data)




class BankViewSet(viewsets.ViewSet):
    
    def queryset():
        queryset = Bank.objects.all()
        return queryset
    
    
    def list(self, request):
        queryset = BankViewSet.queryset()
        serializer = backofficeserializers.BankSerializerGet(queryset, many=True)
        return Response(serializer.data)
   
    
    def retrieve(self, request, pk):
        queryset = BankViewSet.queryset()
        bank = get_object_or_404(queryset, pk=pk)
        serializer = backofficeserializers.BankSerializerGet(bank, many=False)
        return Response(serializer.data)
    
    
    def create(self, request, pk=None):
        serializer = backofficeserializers.BankSerializerPost(data=request.data, many=False)
        
        if Bank.objects.filter(code__iexact=request.data['code']).exists():
            return Response({'Info': f'Banka me kodin {request.data["code"]} ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen!!'})
        
        return Response(serializer.data)
        
        
    
    def update(self, request, pk):
        queryset = BankViewSet.queryset()
        bank = get_object_or_404(queryset, pk=pk)
        serializer = backofficeserializers.BankSerializerPost(instance=bank, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikim!!'})
        return Response(serializer.data)



class BankViewSet(viewsets.ViewSet):
    
    def queryset():
        queryset = Bank.objects.all()
        return queryset
    
    
    def list(self, request):
        queryset = BankViewSet.queryset()
        serializer = backofficeserializers.BankSerializerGet(queryset, many=True)
        return Response(serializer.data)
   
    
    def retrieve(self, request, pk):
        queryset = BankViewSet.queryset()
        bank = get_object_or_404(queryset, pk=pk)
        serializer = backofficeserializers.BankSerializerGet(bank, many=False)
        return Response(serializer.data)
    
    

    def create(self, request, pk=None):
        serializer = backofficeserializers.BankSerializerPost(data=request.data, many=False)
        
        if Bank.objects.filter(code__iexact=request.data['code']).exists():
            return Response({'Info': f'Banka me kodin {request.data["code"]} ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen!!'})
        return Response(serializer.data)
        
        
    
    def update(self, request, pk):
        queryset = BankViewSet.queryset()
        bank = get_object_or_404(queryset, pk=pk)
        serializer = backofficeserializers.BankSerializerPost(instance=bank, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikim!!'})
        return Response(serializer.data)



class MemberTypeViewSet(viewsets.ViewSet):
    
    def queryset():
        queryset = MemberType.objects.all()
        return queryset
    
    def list(self, request):
        queryset = MemberTypeViewSet.queryset()
        serializer = backofficeserializers.MemberTypeSerializerGet(queryset, many=True)
        return Response(serializer.data)
   
    
    def retrieve(self, request, pk):
        queryset = MemberTypeViewSet.queryset()
        memberType = get_object_or_404(queryset, pk=pk)
        serializer = backofficeserializers.MemberTypeSerializerGet(memberType, many=False)
        return Response(serializer.data)
    
    

    def create(self, request, pk=None):
        serializer = backofficeserializers.MemberTypeSerializerPost(data=request.data, many=False)
        
        if MemberType.objects.filter(code__contains=request.data['code']).exists():
            return Response({'Info': f'MemberType me kodin {request.data["code"]} ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen!!'})
        
        return Response(serializer.data)
        
    
    def update(self, request, pk):
        memberType = MemberType.objects.get(id=pk)
        serializer = backofficeserializers.MemberTypeSerializerPost(instance=memberType, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikim!!'})
        return Response(serializer.data)
 
 



