from django.shortcuts import render
from .models import Category, News
from src.research.models import Research
from src.courses.models import Course
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


# Create your views here.


class NewsList(generic.ListView):
    queryset = News.objects.all()
    template_name = "news/news.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context["latest"] = News.objects.all()
        context["news"] = self.get_queryset()
        context["special"] = News.objects.filter(is_special="True")
        context["category_list"] = Category.objects.filter(cate_type="news")
        context["category"] = Course.objects.all()
        return context

    def get_queryset(self):
        queryset = super(NewsList, self).get_queryset()
        search_text = self.request.GET.get("search_text", None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) | Q(content__icontains=search_text)
            )
        return queryset


class NewsDetail(generic.DetailView):
    model = News
    template_name = "news/news_detail.html"

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        context["News_list"] = News.objects.all()
        context["special"] = News.objects.filter(is_special="True")
        context["category_list"] = Category.objects.filter(cate_type="news")
        context["category"] = Course.objects.all()
        context["latest"] = News.objects.all()

        return context


class SportList(generic.ListView):
    queryset = News.objects.filter(category="2")
    template_name = "news/sport.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(SportList, self).get_context_data(**kwargs)
        context["sport"] = self.get_queryset()
        context["latest"] = News.objects.all()
        context["sportlist"] = Category.objects.filter(cate_type="sport")
        context["search_text"] = self.request.GET.get("search_text", "")
        context["category_list"] = Category.objects.filter(cate_type="sport")
        context["category"] = Course.objects.all()

        return context

    def get_queryset(self):
        queryset = super(SportList, self).get_queryset()
        search_text = self.request.GET.get("search_text", None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) | Q(content__icontains=search_text)
            )
        return queryset


class SpecialNews(generic.ListView):
    queryset = News.objects.filter(is_special="True")
    template_name = "news/specialnews.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(SpecialNews, self).get_context_data(**kwargs)
        context["news"] = self.get_queryset()
        context["latest"] = News.objects.all()
        context["special"] = News.objects.filter(is_special="True")
        context["category_list"] = Category.objects.filter(cate_type="news")
        context["search_text"] = self.request.GET.get("search_text", "")
        context["category"] = Course.objects.all()
        return context

    def get_queryset(self):
        queryset = super(SpecialNews, self).get_queryset()
        search_text = self.request.GET.get("search_text", None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) | Q(content__icontains=search_text)
            )
        return queryset


class ResearchNews(generic.ListView):
    queryset = News.objects.filter(category="3")
    template_name = "news/research.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super(ResearchNews, self).get_context_data(**kwargs)
        context["sport"] = self.get_queryset()
        context["latest"] = News.objects.all()
        context["sportlist"] = Category.objects.filter(cate_type="sport")
        context["search_text"] = self.request.GET.get("search_text", "")
        context["category_list"] = Category.objects.filter(cate_type="sport")
        context["category"] = Course.objects.all()

        return context

    def get_queryset(self):
        queryset = super(ResearchNews, self).get_queryset()
        search_text = self.request.GET.get("search_text", None)
        if search_text:
            queryset = queryset.filter(
                Q(title__icontains=search_text) | Q(content__icontains=search_text)
            )
        return queryset