from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static



urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('user_profile.urls')),
    path('shop/', include('shop.urls')),
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

