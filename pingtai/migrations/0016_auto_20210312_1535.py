# Generated by Django 3.1.4 on 2021-03-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pingtai', '0015_dynamicflag'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicflag',
            name='match_name',
            field=models.TextField(blank=True, default=None, verbose_name='比赛名称'),
        ),
        migrations.AddField(
            model_name='dynamicflag',
            name='user_name',
            field=models.TextField(blank=True, default=None, verbose_name='用户名'),
        ),
    ]
