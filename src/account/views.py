from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, CreateAPIView
from rest_framework.viewsets import ViewSetMixin


User = get_user_model()


class UserViewSet(ViewSetMixin,
                  CreateAPIView,
                  RetrieveAPIView,
                  UpdateAPIView,
                  DestroyAPIView):
    queryset = User.objects.all()
