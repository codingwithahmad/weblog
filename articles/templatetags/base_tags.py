from django import template
from ..models import Category, Articles
from django.shortcuts import render
from django.db.models import Count, Q
from datetime import datetime, timedelta
from django.contrib.contenttypes.models import ContentType
# template tags


register = template.Library()


@register.inclusion_tag('articles/partials/navbar_category.html')
def navbar_category():
    category = Category.objects.filter(status=True)
    return { "category": category }

@register.inclusion_tag('articles/partials/sidebar.html')
def popular_articles():
    last_month = datetime.today() - timedelta(days=30)
    articles = Articles.objects.published().annotate(count=Count('hits', filter=Q(articlehit__created__gt=last_month))).order_by('-count', '-publish')[:5]
    return {    "articles": articles,
                "title": "مقالات پر بازدید ماه",
    }


@register.inclusion_tag('articles/partials/sidebar.html')
def hot_articles():
    last_month = datetime.today() - timedelta(days=30)
    content_type_id = ContentType.objects.get(app_label="articles", model="articles").id
    articles = Articles.objects.published().annotate(count=Count('comments', filter=Q(comments__created__gt=last_month) and Q(comments__content_type_id=content_type_id))).order_by('-count', '-publish')[:5]
    return {    "articles": articles,
                "title": "مقالات داغ ماه",
    }



@register.inclusion_tag('registration/partials/link.html')
def link(request, link_name, content, classes):
    return {
        'request': request,
        'link_name': link_name,
        'link': 'account:{}'.format(link_name),
        'content': content,
        'classes': classes,
    }