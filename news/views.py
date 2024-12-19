from django.shortcuts import render, redirect, get_object_or_404
from .models import News



def home(request):
    articles = News.objects.all()
    ctx = {'articles': articles}
    return render(request, 'index.html', ctx)



def news_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        category = request.POST.get('category')
        auther_name = request.POST.get('auther_name')
        if title and short_content and long_content and category and auther_name:
            News.objects.create(
                title=title,
                short_content=short_content,
                long_content=long_content,
                category=category,
                auther_name=auther_name,
            )
            return redirect('home')
    return render(request,'news/add-news.html')



def news_by_category(request, category):
    articles = News.objects.filter(category=category)
    ctx = {'articles': articles, 'category': category}
    return render(request, 'news/news-by-category.html', ctx)


def news_detail(request, news_id):
    articles = get_object_or_404(News, pk=news_id)
    ctx = {'articles': articles}
    return render(request, 'news/detail.html', ctx)
