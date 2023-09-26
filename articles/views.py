from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleListSerializer, ArticleCreateSerializer
from rest_framework.response import Response
from rest_framework import status

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class ArticleDetailView(APIView):
    pass
    

class ArticleAuthorView(APIView):
    pass