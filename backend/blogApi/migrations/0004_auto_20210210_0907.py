# Generated by Django 3.1.6 on 2021-02-10 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogApi', '0003_auto_20210210_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='likedBy',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='likedBy',
            field=models.ManyToManyField(blank=True, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
