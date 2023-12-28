from .serializers import *
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth import update_session_auth_hash





@api_view(['POST'])
def register_user(request):
   if request.method == 'POST':
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def user_login(request):
   if request.method == 'POST':
       username = request.data.get('username')
       password = request.data.get('password')


       user = None
       if '@' in username:
           try:
               user = CustomUsers.objects.get(email=username)
           except ObjectDoesNotExist:
               pass


       if not user:
           user = authenticate(username=username, password=password)


       if user:
           token, _ = Token.objects.get_or_create(user=user)
           return Response({'token': token.key}, status=status.HTTP_200_OK)


       return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
   if request.method == 'POST':
       try:
           # Delete the user's token to logout
           request.user.auth_token.delete()
           return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
       except Exception as e:
           return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class genderViewSet(viewsets.ModelViewSet):
    queryset = gender.objects.all()
    serializer_class = genderSerializer

class DespositvesViewSet(viewsets.ModelViewSet):
    queryset = Despositves.objects.all()
    serializer_class = DespositvesSerializer