# Generated by Django 3.1.6 on 2021-02-11 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApi', '0005_auto_20210211_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='me', max_length=100),
        ),
    ]