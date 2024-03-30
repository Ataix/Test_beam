from django.urls import path

from .views import OrderViewSet

urlpatterns = [
    path('<int:pk>/', OrderViewSet.as_view({
        'post': 'create',
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
]
