from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Articles


# Create your views here.
def home(request):
    content = {
        "articles": Articles.objects.all()
    }
    return render(request, 'articles/articles.html', content)

def details(request, slug):
    content = {
        "article": get_object_or_404(Articles, slug=slug)
    }
    return render(request, 'articles/single.html', content)