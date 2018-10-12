from customizing_auth_practice.models import MyUser
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth')
