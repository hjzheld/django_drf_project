from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleCreateSerializer, CommentSerializer, CommentCreateSerializer
from rest_framework.response import Response
from rest_framework import status

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class ArticleDetailView(APIView):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleListSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.author:
            serializer = ArticleCreateSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('권한이 없습니다', status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.author:
            article.delete()
            return Response('삭제되었습니다', status=status.HTTP_200_OK)
        else:
            return Response('권한이 없습니다', status=status.HTTP_403_FORBIDDEN)
    

class ArticleAuthorView(APIView):
    def get(self, request, author_id):
        article =  Article.objects.filter(author_id=author_id)
        serializer = ArticleListSerializer(article, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class CommentView(APIView):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, article_id):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, article_id=article_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CommentDetailView(APIView):
    def put(self, request, article_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.author:
            serializer = CommentCreateSerializer(
                comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('권한이 없습니다!', status=status.HTTP_403_FORBIDDEN)
        
    def delete(self, request, article_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.author:
            comment.delete()
            return Response('삭제되었습니다!', status=status.HTTP_200_OK)
        else:
            return Response('권한이 없습니다!', status=status.HTTP_403_FORBIDDEN)