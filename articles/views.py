from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles


# Create your views here.
def home(request):
    content = {
        "articles": Articles.objects.all()
    }
    return render(request, 'articles/articles.html', content)