from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from user_auth.serializers import RegisterSerializer

"""
Add custom claims to payload :
Default payload includes the user_id.
You can add any information you want, you just have to modify the claim.
So, Here we are adding username in JWT payloads.
for this, i have created MyTokenObtainPairSerializer & MyObtainTokenPairView

"""


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
