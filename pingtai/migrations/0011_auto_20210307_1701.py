# Generated by Django 3.1.4 on 2021-03-07 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pingtai', '0010_auto_20210307_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uphistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('match_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('upload_flag', models.TextField()),
                ('if_cheating', models.CharField(choices=[('1', '是'), ('0', '否')], max_length=1, verbose_name='是否疑似作弊')),
            ],
            options={
                'verbose_name': '选手答题记录',
                'verbose_name_plural': '选手答题记录',
            },
        ),
        migrations.AlterModelOptions(
            name='achievement',
            options={'verbose_name': '成绩及解答题目', 'verbose_name_plural': '成绩及解答题目'},
        ),
        migrations.AlterModelOptions(
            name='ctfcategory',
            options={'verbose_name': 'CTF 类型管理', 'verbose_name_plural': 'CTF 类型管理'},
        ),
        migrations.AlterModelOptions(
            name='ctfquestions',
            options={'verbose_name': 'CTF 题库管理', 'verbose_name_plural': 'CTF 题库管理'},
        ),
        migrations.AlterModelOptions(
            name='matchinfo',
            options={'verbose_name': '赛事信息管理', 'verbose_name_plural': '赛事信息管理'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name': '通知公告', 'verbose_name_plural': '通知公告'},
        ),
        migrations.AlterModelOptions(
            name='writeup',
            options={'verbose_name': '选手解题解析（WriteUp）', 'verbose_name_plural': '选手解题解析（WriteUp）'},
        ),
        migrations.AlterField(
            model_name='ctfquestions',
            name='docker_file',
            field=models.FileField(blank=True, upload_to='./static/upload/upload_docker_file', verbose_name='部署到Docker的文件'),
        ),
    ]