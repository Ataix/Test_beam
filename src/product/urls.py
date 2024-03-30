from django.urls import path

from .views import ProductViewSet, ShopViewSet

urlpatterns = [
    path('<int:pk>/', ProductViewSet.as_view({
        'post': 'create',
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
    path('shop/<int:pk>/', ShopViewSet.as_view({
        'post': 'create',
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
]
