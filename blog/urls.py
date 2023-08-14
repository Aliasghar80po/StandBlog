from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name="article_detail"),
    path('list/', views.ArticleListView.as_view(template_name='blog/article_list.html'), name="articles_list"),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
    path('contactus/', views.MessageCreateView.as_view(), name="contactus"),
    path('search/', views.search_articles, name="search_articles"),
    path('like/<slug>/<int:pk>', views.like, name="like"),
]