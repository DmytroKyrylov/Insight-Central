from unicodedata import category

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, CreateView
from .models import News, Category
from .forms import NewsForm
from django.urls import reverse_lazy


class HomeNews(ListView):
    model = News
    template_name = "news/home_news_list.html"
    context_object_name = 'news'
    #extra_context = {'title':'Glavanaya'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Main page"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class ViewNews(DeleteView):
    model = News # берет pk с модели
    context_object_name = 'news_item'
    #pk_url_kwarg = 'news_id'
    #template_name = "news/home_news_list.html"  можно использовать другой шаблон, сейчас по умолчанию news_confirm_delete.html


# def index(request): #вместо нее class HomeNews
#     news = News.objects.all()
#     context = {
#         'news':news,
#         'title': 'List of news',
#     }
#     return render(request, 'news/index.html', context)

class CategoryNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk = self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id = self.kwargs['category_id'], is_published=True)


# def get_category(request, category_id): #вместо него class CategotyNews
#     news = News.objects.filter(category_id = category_id)
#     category = Category.objects.get(pk = category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})

# def view_news(request, news_id):  # вместо нее class ViewNews
#     #news_item = News.objects.get(pk = news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render (request, 'news/view_news.html', {"news_item":news_item})

# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#
#     else:
#         form = NewsForm()
#     return render(request,'news/add_news.html', {'form':form})

class CreateNews (CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home') #cтроит маршрут тогда когда это необходимо, home прописан в url



