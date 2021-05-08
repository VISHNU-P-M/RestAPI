

from django.urls import path
from .import views
urlpatterns = [
    path('article/',views.article_list),
    path('article/<int:id>/',views.specific_article),
    path('article-class/', views.ArticleClass.as_view()),
    path('article-class/<int:id>/', views.SpecificClass.as_view()),
    path('generic-class/', views.GenericArticles.as_view()),
    path('generic-class/<int:id>/', views.GenericArticles.as_view()),
]