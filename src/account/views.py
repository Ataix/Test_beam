from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(ViewSetMixin,
                  RetrieveAPIView,
                  UpdateAPIView,
                  DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class PageView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'page.html'
    
    def get(self, request):
        return Response({'message': 'ok'})
