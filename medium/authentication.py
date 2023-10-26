from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomJWTAuthentication(JWTAuthentication):
    def verify(self, token):
        # Add your custom logic to check token validity here, if needed
        return token

    def authenticate(self, request):
        auth = super().authenticate(request)

        if not auth:
            return None

        user, token = auth

        if not self.verify(token):
            raise AuthenticationFailed('Token is invalid or expired')

        return user, token
