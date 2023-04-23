from django.urls import path, include
from rest_framework import routers
from ecommerce.api import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/', include('ecommerce.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
