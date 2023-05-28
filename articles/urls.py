from django.urls import path
from .views import home_view, article_home_view, article_search_view, article_create_view

urlpatterns = [
    path('', home_view),
    path('articles/', article_search_view),
    path('articles/create', article_create_view),
    path('articles/<int:id>/', article_home_view)
]
