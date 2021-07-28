from django import template
from ..models import Category
from django.shortcuts import render
# template tags


register = template.Library()


@register.inclusion_tag('articles/partials/navbar_category.html')
def navbar_category():
    category = Category.objects.filter(status=True)
    return { "category": category }