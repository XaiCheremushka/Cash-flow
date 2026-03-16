from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.permissions import IsAdminUser

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('category/<identifier>/subcategory/', views.SubcategoriesByCategoryAPIView.as_view(), name='subcategory-by-category'),
    path('type/<identifier>/category/', views.CategoriesByTypesAPIView.as_view(), name='type-by-category'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema', permission_classes=[IsAdminUser]), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema', permission_classes=[IsAdminUser]), name='redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)