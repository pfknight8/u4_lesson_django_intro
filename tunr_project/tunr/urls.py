#tunr/urls.py
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('', views.ArtistList.as_view(), name='artist_list'),
  path('songs', views.SongList.as_view(), name='song_list'),
  path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
  path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),
  #Below is for more controlled authenticated page test.
  path('artists', views.ArtistViewSet.as_view({'get': 'list', 'post': 'create'}), name='artist-list')
]