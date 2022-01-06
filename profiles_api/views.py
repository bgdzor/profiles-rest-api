from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers, models
from profiles_api import permissions

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message':f"PUT {pk}"})

    def patch(self, request, pk=None):
        """ Handle a partial of a object"""
        return Response({'message':f"patch {pk}"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'message':f"delete {pk}"})

class HellowViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a Hello message"""
        a_viewset = [
            'Uses actions(list, create, retreive, update, partial_update)',
            'Automatically maps to URLS using routers',
            'Privides more functionality with less code'
        ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None):
        """Handle getting an object by id"""
        return Response({'message':f'Get {pk}'})

    def update(self, request, pk=None):
        """Handle updating an object by id"""
        return Response({'message':'Update'})

    def partial_update(self, request, pk=None):
        """Handle updating part oh an object """
        return Response({'message':'Partial Update'})

    def destroy(self, request, pk=None):
        """Handle removing an object """
        return Response({'message':f'delete {pk}'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Hande creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', )
