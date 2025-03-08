from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from news.models import NewsVarity

# from django.contrib.auth.decorators import login_required

def home(request):
    news = NewsVarity.objects.all()[:3]
    return render(request, 'home.html', {'news' : news})


