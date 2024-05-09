# from django.urls import path
# from .views import PostDetailView, PostListView, UserListView, UserDetailView
from .views import UserViewSet, PostViewSet
from rest_framework.routers import SimpleRouter
#
# urlpatterns = [
#     path('posts/', PostListView.as_view(), name='post-list'),
#     path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
#     path('users/', UserListView.as_view(), name='user-list'),
#     path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
# ]
#
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = router.urls
