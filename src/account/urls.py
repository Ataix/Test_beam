from django.urls import path

from .views import UserViewSet, PageView, UserCreateView

urlpatterns = [
    path('<int:pk>/', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
    path('create/', UserCreateView.as_view()),
    path('wbs/', PageView.as_view())
]
