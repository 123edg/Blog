# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', max_length=30, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_detele', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_detele', models.BooleanField(default=False)),
                ('title', models.CharField(verbose_name='文章标题', max_length=20)),
                ('view_count', models.IntegerField(verbose_name='浏览量', default=0)),
                ('comment_count', models.IntegerField(verbose_name='评论量', default=0)),
                ('context', tinymce.models.HTMLField(verbose_name='文章正文')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_detele', models.BooleanField(default=False)),
                ('user', models.CharField(verbose_name='评论人名称', max_length=10)),
                ('emil', models.CharField(verbose_name='邮箱', max_length=20, null=True)),
                ('web', models.CharField(verbose_name='网站名称', max_length=20, null=True)),
                ('content', models.TextField(verbose_name='评论内容')),
                ('comment', models.ForeignKey(verbose_name='评论的文章', to='blogapp.Article')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_detele', models.BooleanField(default=False)),
                ('user', models.CharField(verbose_name='联系人名称', max_length=10)),
                ('emil', models.CharField(verbose_name='邮箱', max_length=20, null=True)),
                ('subject', models.CharField(verbose_name='主题名称', max_length=10, null=True)),
                ('content', models.TextField(verbose_name='评论内容')),
            ],
            options={
                'verbose_name': '联系',
                'verbose_name_plural': '联系',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_detele', models.BooleanField(default=False)),
                ('name', models.CharField(verbose_name='分类名称', max_length=10, default='默认分类')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
                'db_table': 'sort',
            },
        ),
        migrations.CreateModel(
            name='Tages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_detele', models.BooleanField(default=False)),
                ('name', models.CharField(verbose_name='标签名称', max_length=10, default='默认分类')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
                'db_table': 'tages',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='sort',
            field=models.ForeignKey(verbose_name='所属分类', to='blogapp.Sort'),
        ),
        migrations.AddField(
            model_name='article',
            name='tages',
            field=models.ManyToManyField(verbose_name='标签', to='blogapp.Tages'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL),
        ),
    ]
