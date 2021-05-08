from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins

# Create your views here.
class GenericArticles(generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
    
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    
    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self, request, id=None): 
        return self.create(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id):
        return self.destroy(request,id)



class ArticleClass(APIView):
    
    def get(self, request):
        articles = Article.objects.all()
        article_serial = ArticleSerializer(articles, many=True)
        return Response(article_serial.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpecificClass(APIView):
    
    def get_obj(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Http404()
        
    def get(self, request, id):
        article = self.get_obj(id)
        serialize = ArticleSerializer(article)
        return Response(serialize.data)
    
    def put(self, request, id):
        article = self.get_obj(id)
        serialize = ArticleSerializer(article, data=request.data)
        
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        article = self.get_obj(id)
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT) 
        


@api_view(['GET', 'POST']) 
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        article_serial = ArticleSerializer(articles, many=True)
        return Response(article_serial.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass


@api_view(['GET', 'PUT', 'DELETE'])
def specific_article(request,id):
    try:
        article = Article.objects.get(id=id)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialize = ArticleSerializer(article)
        return Response(serialize.data)
    elif request.method == 'PUT':
        serialize = ArticleSerializer(article, data=request.data)
        
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        
        