from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from reviews.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('', include(router.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
