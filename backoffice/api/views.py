from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, MemberSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from backoffice.models import Member, MemberType
import jwt, datetime
from django.contrib import auth



class LoginView(APIView):
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        else:
            refresh = RefreshToken.for_user(user)
            user.last_login = datetime.datetime.now()
            user.save()
            member = Member.objects.filter(user_id=user.id).first()
            
            response = {
                'access_token': str(refresh.access_token),
                'refreshToken': str(refresh),
                'member': MemberSerializer(member).data,
                'memberType': member.memberType.code
                # 'permissions': self.getPermissions(user)
            } 

        return Response(response, status.HTTP_201_CREATED)
    
    
    

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request):
        print(request.user)
        auth.logout(request)
        response = Response()
        response.data = {
            'message': 'success'
                }
        print(request.headers.get('Authorization'))
        print(request.user)
                 
        return response
