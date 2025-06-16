from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, UserRegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(email=request.data['email'])
        response.data['user'] = {
            'email': user.email,
            'username': user.username,
        }
        return response