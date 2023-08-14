from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category, Message, Like
from django.core.paginator import Paginator
from .forms import MessageForm
from django.http import Http404, JsonResponse
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView


# from django.urls import reverse_lazy


def Article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/article_details.html', {'article': article, 'articles': Article.objects.all()})


def Article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    object_list = paginator.get_page(page_number)
    return render(request, "blog/article_list.html", {'article': object_list, 'articles': Article.objects.all()})


def contactus(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            Message.objects.create(title=title, text=text, email=email, age=age)
    else:
        form = MessageForm()
    return render(request, 'blog/contact_us.html', {'form': form, 'articles': Article.objects.all()})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.article_set.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {'article': object_list, 'articles': Article.objects.all()})


def search_articles(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    object_list = paginator.get_page(page_number)
    if request.method == 'GET':
        search_value = request.GET.get('q', '')  # مقدار فیلد سرچ را دریافت می‌کنیم
        return render(request, "blog/article_list.html",
                      {'article': object_list, 'search_value': search_value, 'articles': Article.objects.all()})


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context


# class ContactUsView(FormView):
#     template_name = 'blog/contact_us.html'
#     success_url = reverse_lazy('home:main')
#     form_class = MessageForm
#
#     def form_valid(self, form):
#         form_data = form.cleaned_data
#         Message.objects.create(title=form_data['title'])
#         return super().form_valid(form)

# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'blog/article_details.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['articles'] = Article.objects.all()
#         return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        if self.request.user.likes.filter(article__slug=self.object.slug, user_id=self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context

class MessageCreateView(UserPassesTestMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'blog/contact_us.html'
    success_url = "/"

    # fields = ['title', 'text', 'date', 'age']====> اگراز مدل استفاده میکردیم
    # model = Message  مدلی که می‌خواهید از آن برای ایجاد رکورد جدید استفاده کنید
    # form_class = MessageForm: فرمی که می‌خواهید برای ایجاد رکورد استفاده کنید. این فرم در اینجا
    def form_valid(self, form):
        instance = form.save(commit=False)
        if self.request.user.is_authenticated:
            instance.email = self.request.user.email
        instance.date = timezone.now()
        instance.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        raise Http404("To access this page, you need to be logged in.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = 'article'
        context['articles'] = Article.objects.all()
        return context


def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug, user_id=request.user.id)
        like.delete()
        return JsonResponse({'response': 'unliked'})
    except:
        Like.objects.create(article_id=pk, user_id=request.user.id)
        return JsonResponse({'response': 'liked'})



# def like(request, slug, pk):
#     try:
#         like = Like.objects.get(article__slug=slug, user_id=request.user.id)
#         like.delete()
#         return JsonResponse({'response': 'unliked'})
#     except Like.DoesNotExist:
#         Like.objects.create(article__id=pk, user_id=request.user.id)
#         return JsonResponse({'response': 'liked'})
#     except Exception as e:
#         return JsonResponse({'response': 'error', 'message': str(e)})




# def like(request, slug, pk):
#     try:
#         like = Like.objects.get(article__slug=slug, user=request.user)
#         like.delete()
#         return JsonResponse({'response': 'unliked'})
#     except Like.DoesNotExist:
#         Like.objects.create(article_id=pk, user=request.user)
#         return JsonResponse({'response': 'liked'})
#     except Exception as e:
#         return JsonResponse({'response': 'error', 'message': str(e)})


from django.shortcuts import get_object_or_404
from django.http import JsonResponse

#
# def like(request, slug, pk):
#     article = get_object_or_404(Article, slug=slug)
#
#     try:
#         like = Like.objects.get(article=article, user=request.user)
#         like.delete()
#         response_data = {'response': 'unliked'}
#     except Like.DoesNotExist:
#         Like.objects.create(article=article, user=request.user)
#         response_data = {'response': 'liked'}
#     except Exception as e:
#         response_data = {'response': 'error', 'message': str(e)}
#
#     return JsonResponse(response_data)

