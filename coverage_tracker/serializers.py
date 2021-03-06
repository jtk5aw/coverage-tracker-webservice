from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Staffer


class StafferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staffer
        fields = ['comp_id', 'staffer_type', 'name', 'building', 'on_coverage', 'phone_number']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']