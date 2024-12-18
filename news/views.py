from django.shortcuts import render,redirect
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
        if title and short_content and long_content and category:
            News.objects.create(
                title=title,
                short_content=short_content,
                long_content=long_content,
                category=category
            )
            return redirect('home')
    return render(request,'news/add-news.html')



def news_by_category(request, category):
    pass


def news_detail(request, news_id):
    pass
