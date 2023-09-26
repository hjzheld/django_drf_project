from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from articles.serializers import ArticleListSerializer, CommentSerializer


# 프로필
class UserProfileSerializer(serializers.ModelSerializer):
    # 글 조회
    article_set = ArticleListSerializer(many=True)
    # 댓글 조회 
    comment_set = CommentSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'fullname', 'nickname', 'date_of_birth', 'article_set', 'comment_set']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
        
        

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token