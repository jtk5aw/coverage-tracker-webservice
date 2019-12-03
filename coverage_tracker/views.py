from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .models import Staffer
from .serializers import UserSerializer, GroupSerializer, StafferSerializer

class StafferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Staffers to be viewed or edited.
    """
    queryset = Staffer.objects.all()
    serializer_class = StafferSerializer
    http_method_names = ['get', 'post', 'put']

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['get']


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get']