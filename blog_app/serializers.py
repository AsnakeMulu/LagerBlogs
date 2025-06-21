from rest_framework import serializers
from .models import Post, Comment, User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return {
            "id": obj.author.id,
            "username": obj.author.username,
            "email": obj.author.email,
        }

    class Meta:
        model = Post
        fields = ['id', 'title', 'caption', 'slug', 'content', 'created_at', 'author']

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'created_at']
        read_only_fields = ['author', 'created_at']