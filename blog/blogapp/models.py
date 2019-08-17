from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel
from tinymce.models import HTMLField
# Create your models here.


class User(AbstractUser,BaseModel):
    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username


class Sort(BaseModel):
    '''分类'''
    name = models.CharField(max_length=10,default='默认分类',null=False,verbose_name='分类名称')#分类


    def __str__(self):
        return self.name

    class Meta:
        db_table='sort'
        verbose_name = '文章分类'
        verbose_name_plural=verbose_name


class Tages(BaseModel):
    '''标签'''
    name = models.CharField(max_length=10,default='默认分类',null=False,verbose_name='标签名称')#标签


    def __str__(self):
        return self.name


    class Meta:
        db_table='tages'
        verbose_name = '文章标签'
        verbose_name_plural=verbose_name


class Article(BaseModel):
    '''文章'''
    user = models.ForeignKey('User',verbose_name='作者')#作者
    sort = models.ForeignKey('Sort',verbose_name='所属分类')#分类
    tages = models.ManyToManyField('Tages',verbose_name='标签')#标签
    #introduce = HTMLField(verbose_name='简介')
    title = models.CharField(max_length=20,null=False,verbose_name='文章标题')#文章标题
    view_count = models.IntegerField(default=0,verbose_name='浏览量')#文章浏览量
    comment_count = models.IntegerField(default=0,verbose_name='评论量')#评论量
    context = HTMLField(verbose_name='文章正文')

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Comment(BaseModel):
    user = models.CharField(max_length=10,verbose_name='评论人名称')#评论人
    emil = models.CharField(max_length=20,null=True,verbose_name='邮箱')
    web = models.CharField(max_length=20,null=True,verbose_name='网站名称')
    content = models.TextField(verbose_name='评论内容',null=False)
    comment = models.ForeignKey('Article',null=False,verbose_name='评论的文章')


    def __str__(self):
        return self.content


    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural=verbose_name


class Contact(BaseModel):
    user = models.CharField(max_length=10, verbose_name='联系人名称')  # 评论人
    emil = models.CharField(max_length=20, null=True, verbose_name='邮箱')
    subject = models.CharField(max_length=10, null=True, verbose_name='主题名称')
    content = models.TextField(verbose_name='评论内容', null=False)

    def __str__(self):
        return self.subject

    class Meta:
        db_table = 'contact'
        verbose_name = '联系'
        verbose_name_plural=verbose_name
