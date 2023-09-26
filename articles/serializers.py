from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.nickname

    class Meta:
        model = Article
        fields = '__all__'
        
        
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "image", "content")
        
        
class ArticleListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(serlf, obj):
        return obj.author.nickname

    class Meta:
        model = Article
        fields = ['pk', 'title', 'content', 'image', 'updated_at', 'author']