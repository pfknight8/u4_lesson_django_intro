from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import ArtistSerializer, SongSerializer
from .models import Artist, Song
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

# Create your views here.
class ArtistList(generics.ListCreateAPIView):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer
  permission_classes = [IsAdminUser]

class SongList(generics.ListCreateAPIView):
  queryset = Song.objects.all()
  serializer_class = SongSerializer

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Song.objects.all()
  serializer_class = SongSerializer

# What about these instead? Useful for adding authentication in.

class ArtistViewSet(viewsets.ModelViewSet):
  queryset = Artist.objects.all()
  serializer_class = ArtistSerializer
  permission_classes_by_action = {'create': [IsAdminUser], 'list': [IsAuthenticated]}
  
  def create(self, request, *args, **kwargs):
    return super(ArtistViewSet, self).create(request, *args, **kwargs)
  
  def list(self, request, *args, **kwargs):
    return super(ArtistViewSet, self).list(request, *args, **kwargs)

  def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
