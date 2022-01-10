from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


class GetNodes(generics.ListCreateAPIView):
    serializer_class = NodeListSerializer
    queryset = Node.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Node.objects.all()
        queryset = queryset.filter(user=user)
        return queryset


class UpdateNodes(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NodeListSerializer
    queryset = Node.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Node.objects.all()
        queryset = queryset.filter(user=user)
        return queryset


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}

        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            data['response'] = 'User created successfully'
            data['email'] = user.email
            data['username'] = user.username
        return Response(data)
