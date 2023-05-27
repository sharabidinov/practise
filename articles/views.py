import random
from django.shortcuts import render, HttpResponse
from .models import Article


# Create your views here.
def home_view(request):
    article_obj = Article.objects.all()
    context_data = {
        'context_data': article_obj
    }
    return render(request, context=context_data, template_name='home-view.html')


def article_home_view(request, id=None):
    article_object = Article.objects.get(id=id)
    context_data = {
        "article_object": article_object
    }
    return render(request, context=context_data, template_name='home-detail-view.html')


def article_search_view(request):
    query_dict = request.GET
    try:
        query = int(query_dict.get('query'))
    except:
        query = None
    article_object = None
    if query is not None:
        article_object = Article.objects.get(id=query)
    context = {'article_object': article_object}
    return render(request, context=context, template_name='search.html')
