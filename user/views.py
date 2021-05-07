from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt 
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        article_serial = ArticleSerializer(articles, many=True)
        return JsonResponse(article_serial.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
        
    elif request.method == 'PUT':
        pass
    else:
        pass


@csrf_exempt
def specific_article(request,id):
    try:
        article = Article.objects.get(id=id)
    except:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serialize = ArticleSerializer(article)
        return JsonResponse(serialize.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialize = ArticleSerializer(article, data=data)
        
        if serialize.is_valid():
            serialize.save()
            return JsonResponse(serialize.data, status=200)
        else:
            return JsonResponse(serialize.errors, status=400)
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
        
        