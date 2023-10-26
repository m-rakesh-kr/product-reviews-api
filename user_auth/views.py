from datetime import datetime
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenBlacklistView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ChangePasswordSerializer, UpdateUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from user_auth.serializers import RegisterSerializer

"""
Add custom claims to payload :
Default payload includes the user_id.
You can add any information you want, you just have to modify the claim.
So, Here we are adding username in JWT payloads.
for this, i have created MyTokenObtainPairSerializer & MyObtainTokenPairView

"""


# class MyObtainTokenPairView(TokenObtainPairView):
#     permission_classes = (AllowAny,)
#     serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

# class LogoutView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#         try:
#             refresh_token = request.data.get("refresh_token")  # Use get to avoid KeyError if 'refresh_token' is missing
#             # print(f"Request Data:-{request.data}")
#             print(f"Refresh Token:-{refresh_token}")
#             # print(f"Access Token:-{refresh_token.access_token}")
#             token = RefreshToken(refresh_token)
#             print(token.access_token)
#
#             # Check if the token is already blacklisted
#             if BlacklistedToken.objects.filter(token=token.jti).exists():
#                 return Response({'detail': 'Token already blacklisted.'}, status=status.HTTP_400_BAD_REQUEST)
#
#             token.blacklist()
#             return Response({'detail': 'Logged out successfully'}, status=status.HTTP_200_OK)
#
#         except Exception as e:
#             return Response({'error': 'Invalid request. Please provide a valid refresh token.'},
#                             status=status.HTTP_400_BAD_REQUEST)
#
#
# class LogoutAllView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#         # Get all outstanding tokens for the current user
#         tokens = OutstandingToken.objects.filter(user_id=request.user.id)
#
#         # Blacklist each token
#         for token in tokens:
#             RefreshToken(token.token).blacklist()
#
#         # Return a response indicating successful logout
#         return Response({'detail': 'Logged out from all devices successfully'}, status=status.HTTP_200_OK)
