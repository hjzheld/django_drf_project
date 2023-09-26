from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleListSerializer
from rest_framework.response import Response
from rest_framework import status

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ArticleDetailView(APIView):
    pass