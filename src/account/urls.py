from django.urls import path

from .views import UserViewSet

urlpatterns = [
    path('<int:pk>/', UserViewSet.as_view({
        'post': 'create',
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
]
