from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


# Create your views here.
class HelloApiView(APIView):
    """Test Api view """

    serializer_class= serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a tradtional Django View',
            'Tanmay',
            'Is mapped manually to URLs'
        ]

        return Response({'message':"Hello!", 'an_apiview':an_apiview})

    def put(self, request, pk=None):
        """Handle Updating a object"""

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""

        return Response({'method': 'PATCH'})

    def post(self, request):
        """Create a hello message with our name"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """Handle deletion of object"""

        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Create a demo View set"""

    serializer_class= serializers.HelloSerializer

    def list(self, request):
        """Return a mesg"""

        a_viewset= [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Create View set"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self, request, pk=None):
        """Handle for getting an object"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle for updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle for partially updating obj"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle for deleting obj"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profile"""
    serializer_class=serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,) # To create it as tuple
    permission_classes = (permissions.UpdateOwnProfile,)
