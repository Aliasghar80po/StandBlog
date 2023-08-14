from django.shortcuts import render
from blog.models import Article
from django.views.generic import RedirectView , ListView
# Create your views here.
def home(request):
    article = Article.objects.all()
    # recent_articles = Article.objects.all()[:2]
    return render(request,'home/index.html', {'article': article, 'articles':Article.objects.all()})

# 'articles';articles no articles : 'articles' :/

def sidebar(request):
    recent_articles = Article.objects.all().order_by('-created')
    return render(request, 'includes/sidebar.html', {'recent_articles': recent_articles, 'articles':Article.objects.all()})
#این تابع برای رندر پارشیال نوشته شدومیتواند کار کانتکست پروسسرز را هم انجام دهد
#حتی میتوان فقط سایدبار را رندر کرد و بجای ریسنت چیزهای دیگری نشان داد مثلا تگها



