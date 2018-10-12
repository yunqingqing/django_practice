from customizing_auth_practice.models import MyUser
from rest_api.serializers import UserSerializer

from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all().order_by('-date_of_birth')
    serializer_class = UserSerializer
