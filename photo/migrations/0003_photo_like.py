# Generated by Django 2.2 on 2019-05-02 04:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0002_auto_20190501_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='like',
            field=models.ManyToManyField(related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
