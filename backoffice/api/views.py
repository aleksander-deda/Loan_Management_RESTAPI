from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from backoffice.models import Member, MemberType
import jwt, datetime



class LoginView(APIView):
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='access_token', value=token, httponly=True)
        
        response.data = {'access_token': token}
        
        return response
    
    
    def get(self, request):
        
        token = request.COOKIES.get('access_token')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')	
        
        user = User.objects.filter(id=payload['id']).first()
        
        member = Member.objects.filter(user_id=user.id).first()
        memberTypeId =  member.memberType_id
        memberType = MemberType.objects.filter(id=memberTypeId).first()
        memberTypeCode = memberType.code
        
        if user and memberTypeCode == "partner":
            return Response({'The Logged in user is "Partner"'})
        
        if user and memberTypeCode == "account_manager":
            return Response({'The Logged in user is "Account Manager"'})
        
        if user and memberTypeCode == "underwriter":
            return Response({'The Logged in user is "Underwriter"'})
        
        if user and memberTypeCode == "super_admin":
            return Response({'The Logged in user is "SuperAdmin"'})
        
        serializer = UserSerializer(user)
        
        
        return Response(serializer.data)
    
    


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('access_token')
        response.data = {
            'message': 'success'
                }
        
        return response