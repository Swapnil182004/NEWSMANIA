from django.shortcuts import render
from .models import NewsVarity
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url= "login")
def all_news(request):
    all_news = NewsVarity.objects.all()
    return render(request, 'all_news.html', {'all_news': all_news})

@login_required(login_url= "login")
def news_details(request, news_id):
    one_news = get_object_or_404(NewsVarity, pk = news_id)
    return render(request, 'news_details.html', {'news': one_news})
