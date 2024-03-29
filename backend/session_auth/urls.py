from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view as drf_get_schema_view
from drf_yasg.views import get_schema_view as yasg_get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = yasg_get_schema_view(
    openapi.Info(
        title="Online Shop API",
        default_version="v1",
        description="API Docs for Online Shop",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="lumumbaclement@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('user_profile.urls')),
    path('shop/', include('shop.urls')),
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
