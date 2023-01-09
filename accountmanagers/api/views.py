from rest_framework.response import Response
from rest_framework import serializers, viewsets
from partners.api.serializers import PartnerSerializerGET, PartnerSerializerPOST
from partners.models import Partner
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import action




class PartnerViewSet(viewsets.ModelViewSet):
    
    def queryset():
        queryset = Partner.objects.all()
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
        queryset = PartnerViewSet.queryset()
        partner = get_object_or_404(queryset, pk=pk)
        serializer = PartnerSerializerPOST(instance=partner, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'Info': f'Te dhenat e Partnerit {serializer.data["name"]} u modifikuan me sukses! Ne pritje te konfirmimit.'})

        else:
            return Response({'Error': 'Nuk keni plotesuar sakte formen per modifikimin e Partnerit !!'})
    
    
 
    def confirmPartner(self, request, pk):
        print('enter in confirmation')
        try:
            partner = Partner.objects.get(id=pk)
            partner.isActive = True
            partner.isConfirmed = True
            partner.save()
            return Response({'Info': f'Partneri {partner.member.user.first_name} {partner.member.user.last_name} u Konfirmua me sukses'})
        
        except:
            return Response({'Info': f'Partneri {partner.name} nuk u Konfirmua !'})
        
    
    def confirmModifiedPartner(self, request, pk):
        print('enter in confirmation')
        try:
            partner = Partner.objects.get(id=pk)
            partner.isActive = True
            partner.isConfirmed = True
            partner.save()
            return Response({'Info': f'Partneri {partner.member.user.first_name} {partner.member.user.last_name} u Konfirmua me sukses'})
        
        except:
            return Response({'Info': f'Partneri {partner.name} nuk u Konfirmua !'})

        
        
    
    
    
    
    