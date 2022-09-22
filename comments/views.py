from rest_framework import generics, permissions
from API.permissions import IsOwnerOrReadOnly
from .models import Comments
from .serializers import CommentsSerializer, CommentsDetailSerializer

class CommentsList(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comments.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentsDetailSerializer
    queryset = Comments.objects.all()
