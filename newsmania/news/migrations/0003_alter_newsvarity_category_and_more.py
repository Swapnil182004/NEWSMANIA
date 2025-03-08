# Generated by Django 5.1.6 on 2025-03-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsvarity_author_newsvarity_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsvarity',
            name='category',
            field=models.CharField(choices=[('SPORTS', 'SPORTS'), ('BUSINESS', 'BUSINESS'), ('TECHNOLOGY', 'TECHNOLOGY'), ('POLITICS', 'POLITICS'), ('STOCK', 'STOCK')], max_length=20),
        ),
        migrations.AlterField(
            model_name='newsvarity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='newsvarity',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='news_thumbs/'),
        ),
    ]
