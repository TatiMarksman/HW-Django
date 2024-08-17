from django.shortcuts import render
from articles.models import Article

def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'

    articles = Article.objects.order_by(ordering).prefetch_related('scopes__tag')

    context = {
        'articles': articles,
    }

    return render(request, template, context)
