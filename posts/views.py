# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorReadOnly
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet


#
# class PostListView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class UserListView(ListCreateAPIView):
#     permission_classes = (IsAdminUser,)
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetailView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAdminUser,)
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorReadOnly,)


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
