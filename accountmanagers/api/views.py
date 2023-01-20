from rest_framework.response import Response
from rest_framework import serializers, viewsets, status
from partners.api.serializers import PartnerSerializerGET, PartnerSerializerPOST
from superpartners.api.serializers import SuperPartnerSerializerGET, SuperPartnerSerializerPOST
from partners.models import Partner
from superpartners.models import SuperPartner
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated




class PartnerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def queryset():
        queryset = Partner.objects.filter(isConfirmed=True, isActive=True)
        return queryset
    
    
    def list(self, request):
        queryset = PartnerViewSet.queryset()
        serializer = PartnerSerializerGET(queryset, many=True)
        return Response(serializer.data)
   
    
    def retrieve(self, request, pk):
        queryset = PartnerViewSet.queryset()
        partner = get_object_or_404(queryset, pk=pk)
        serializer = PartnerSerializerGET(partner, many=False)
        return Response(serializer.data)
    
    

    def create(self, request, pk=None):
        serializer = PartnerSerializerPOST(data=request.data, many=False)
        
        if User.objects.filter(username=request.data["username"]).exists():
            return Response({'Info': f'Perdoruesi me username {request.data["username"]} ekziston tashme!'})
        
        if Partner.objects.filter(nipt=request.data["nipt"]).exists():
            return Response({'Info': f'Partneri me nipt {request.data["nipt"]} ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()
        
        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per Partnerin!!'})
        
        return Response(serializer.data)
        
    
    def update(self, request, pk):
        print(request.user)
        queryset = PartnerViewSet.queryset()
        partner = get_object_or_404(queryset, pk=pk)
        serializer = PartnerSerializerPOST(instance=partner, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'Info': f'Te dhenat e Partnerit {serializer.data["name"]} u modifikuan me sukses! Ne pritje te konfirmimit.'}, status.HTTP_201_CREATED)

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikimin e Partnerit !!'})
    
    
 
    def confirmPartner(self, request, pk):
        print(request.user)
        try:
            partner = Partner.objects.get(id=pk)
            partner.isActive = True
            partner.isConfirmed = True
            partner.save()
            return Response({'Info': f'Partneri {partner.member.user.first_name} {partner.member.user.last_name} u Konfirmua me sukses'}, status.HTTP_201_CREATED)
        
        except:
            return Response({'Info': f'Partneri {partner.name} nuk u Konfirmua !'})
        
    
    def confirmModifiedPartner(self, request, pk):
        print(request.user)
        try:
            partner = Partner.objects.get(id=pk)
            datas = partner.jsonDatas
            partner.bank_id = datas["bank"]
            partner.isActive = datas["isActive"]
            partner.personalId = datas["personalId"]
            partner.nipt = datas["nipt"]
            partner.isReferral = datas["isReferral"]
            partner.rating = datas["rating"]
            partner.accountNumber = datas["accountNumber"]
            partner.jsonDatas = None
            partner.isUpdated = "Yes"
            partner.save()
            return Response({'Info': f'Te dhenat per partnerin {partner.member.user.first_name} {partner.member.user.last_name} u modifikuan me sukses'}, status.HTTP_201_CREATED)
        
        except:
            return Response({'Info': f'Partneri {partner.name} nuk u Konfirmua !'})
        
        

class SuperPartnerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def queryset():
        queryset = SuperPartner.objects.filter()
        return queryset
    
    
    def list(self, request):
        queryset = SuperPartnerViewSet.queryset()
        serializer = SuperPartnerSerializerGET(queryset, many=True)
        return Response(serializer.data)
   
    
    def retrieve(self, request, pk):
        queryset = SuperPartnerViewSet.queryset()
        partner = get_object_or_404(queryset, pk=pk)
        serializer = SuperPartnerSerializerGET(partner, many=False)
        return Response(serializer.data)
    
    

    def create(self, request, pk=None):
        serializer = SuperPartnerSerializerPOST(data=request.data, many=False)
        
        if User.objects.filter(username=request.data["username"]).exists():
            return Response({'Info': f'Perdoruesi me username {request.data["username"]} ekziston tashme!'})
        
        if SuperPartner.objects.filter(nipt=request.data["nipt"]).exists():
            return Response({'Info': f'SuperPartneri me nipt {request.data["nipt"]} ekziston tashme!'})
        
        if SuperPartner.objects.filter(code=request.data["code"]).exists():
            return Response({'Info': f'SuperPartneri me kodin {request.data["code"]} ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()
        
        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per SuperPartnerin!!'})
        
        return Response(serializer.data)
        
    
    def update(self, request, pk):
        print(request.user)
        queryset = SuperPartnerViewSet.queryset()
        partner = get_object_or_404(queryset, pk=pk)
        serializer = SuperPartnerSerializerPOST(instance=partner, data=request.data, partial=True)
        
        if SuperPartner.objects.filter(nipt=request.data["nipt"]).exists():
            return Response({'Info': f'SuperPartneri me nipt {request.data["nipt"]} ekziston tashme!'})
        
        if serializer.is_valid():
            serializer.save()
            return Response({'Info': f'Te dhenat e SuperPartnerit {serializer.data["name"]} u modifikuan me sukses! Ne pritje te konfirmimit.'}, status.HTTP_201_CREATED)

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikimin e SuperPartnerit !!'})
    
    
 
    def confirmSuperPartner(self, request, pk):
        print(request.user)
        try:
            partner = SuperPartner.objects.get(id=pk)
            partner.isActive = True
            partner.isConfirmed = True
            partner.save()
            return Response({'Info': f'SuperPartneri {partner.member.user.first_name} {partner.member.user.last_name} u Konfirmua me sukses'}, status.HTTP_201_CREATED)
        
        except:
            return Response({'Info': f'SuperPartneri {partner.name} nuk u Konfirmua !'})
        
    
    def confirmModifiedSuperPartner(self, request, pk):
        print(request.user)
        try:
            superPartner = SuperPartner.objects.get(id=pk)
            datas = superPartner.jsonDatas
            superPartner.isActive = datas["isActive"]
            superPartner.isDeleted = datas["isDeleted"]
            superPartner.nipt = datas["nipt"]
            superPartner.jsonDatas = None
            superPartner.isUpdated = "Yes"
            superPartner.save()
            return Response({'Info': f'Te dhenat per SuperPartnerin {superPartner.member.user.first_name} {superPartner.member.user.last_name} u modifikuan me sukses'}, status.HTTP_201_CREATED)
        
        except:
            return Response({'Info': f'SuperPartneri {superPartner.name} nuk u Konfirmua !'})
        

        
        
    
    
    
    
    