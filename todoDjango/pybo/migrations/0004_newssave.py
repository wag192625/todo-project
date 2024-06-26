# Generated by Django 5.0.6 on 2024-06-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_alter_todo_importance'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=200)),
                ('news_content', models.CharField(max_length=300)),
                ('news_writing', models.CharField(max_length=20)),
                ('news_image', models.URLField()),
                ('news_link', models.URLField()),
            ],
        ),
    ]
