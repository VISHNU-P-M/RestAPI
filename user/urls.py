

from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', views.ArticleViewset, basename='article' )
router.register('generic-article', views.ArticleGenericViewset, basename='generic-article')
router.register('modal-viewset', views.ArticleModalViewset, basename='modal-viewset')
router.register('generic-crud', views.ArticleGeneric, basename='generic-crud')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('article/',views.article_list),
    path('article/<int:id>/',views.specific_article),
    path('article-class/', views.ArticleClass.as_view()),
    path('article-class/<int:id>/', views.SpecificClass.as_view()),
    path('generic-class/', views.GenericArticles.as_view()),
    path('generic-class/<int:id>/', views.GenericArticles.as_view()),
]