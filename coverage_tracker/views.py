from django.contrib.auth.models import User, Group

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import Staffer
from .serializers import UserSerializer, GroupSerializer, StafferSerializer


@api_view(['GET', 'POST'])
def staffer_list(request, format=None):
    """
    List all staffers, or create a new snippet.
    """
    if request.method == 'GET':
        staffers = Staffer.objects.all()
        print(staffers)
        serializer = StafferSerializer(staffers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StafferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def staffer_by_comp_id(request, comp_id, format=None):
    """
    Retrieve a staffer based on comp_id
    """
    try:
        staffer = Staffer.objects.get(comp_id=comp_id)
    except Staffer.DoesNotExist:
        return Response([])

    if request.method == 'GET':
        serializer = StafferSerializer(staffer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StafferSerializer(staffer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        staffer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def staffer_by_dorm(request, dorm, format=None):
    """
    Retrieve a list of staffers given a dorm name
    """
    staffers = Staffer.objects.filter(building=dorm)


    if request.method == 'GET':
        serializer = StafferSerializer(staffers, many=True)
        return Response(serializer.data)


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