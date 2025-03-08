from django.db import models
from django.utils import timezone

# Create your models here.
class NewsVarity(models.Model):
    NEWS_TYPE = [
        ('SPOTRS', 'SPORTS'),
        ('BUSINESS', 'BUSINESS'),
        ('TECHNOLOGY', 'TECHNOLOGY'),
        ('POLITICS', 'POLITICS'),
        ('STOCK', 'STOCK'),
    ]
    title = models.CharField(max_length=100, default="default title")
    thumbnail =  models.ImageField(upload_to="news_thums/")
    description  = models.TextField(default="default desc")
    author = models.CharField(max_length=100, default="Unknown")
    created_at  = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=20, choices=NEWS_TYPE)

    def __str__(self):
        return self.title
    
