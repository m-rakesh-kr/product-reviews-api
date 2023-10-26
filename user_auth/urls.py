from django.urls import path
from user_auth.views import RegisterView, ChangePasswordView, UpdateProfileView

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenBlacklistView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change-password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('token_blacklist/', TokenBlacklistView.as_view(), name='auth_logout'),

    # path('logout/', LogoutView.as_view(), name='auth_logout'),
    # path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),

]
