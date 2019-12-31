from customizing_auth_practice.models import MyUser
from rest_api.serializers import UserSerializer
from customizing_auth_practice.models import MyUser

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all().order_by('-date_of_birth')
    serializer_class = UserSerializer

class Users(APIView):
    def get(self, request):
        users = MyUser.objects.all()
        serialized = UserSerializer(users, many=True)
        # import pdb; pdb.set_trace()
        return HttpResponse(serialized.data)
        return Response(serialized.data)