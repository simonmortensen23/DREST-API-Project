from rest_framework import generics, permissions
from API.permissions import IsOwnerOrReadOnly
from .models import Likes
from likes.serializers import LikesSerializer

class LikesList(generics.ListCreateAPIView):
    serializer_class = LikesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()