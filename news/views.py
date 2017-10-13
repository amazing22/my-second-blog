from django.shortcuts import render
from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)


def month_archive(request):
    return render(request, 'news/month_archive.html',{})

def article_detail(request, pk):
    a_list = get_object_or_404(Article, pk=pk)
    return render(request, 'news/detail.html',{'a_list' : a_list})
