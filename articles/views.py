from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ArticleSerializer, ArticleListSerializer, ArticleCreateSerializer
from rest_framework.generics import get_object_or_404
# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ArticleDetailView(APIView):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            serializer = ArticleCreateSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        


class CommentView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass


class CommentDetailView(APIView):
    def put(self, request):
        pass

    def delete(self, request):
        pass


class LikeView(APIView):
    def post(self, request):
        pass
    