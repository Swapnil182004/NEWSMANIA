from django.urls import path, include
from . import views

urlpatterns = [
    path("all_news/", views.all_news, name="all_news"),
    path("<int:news_id>", views.news_details, name="news_details")
]
