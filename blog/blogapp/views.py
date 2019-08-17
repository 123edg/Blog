from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from django.core.urlresolvers import reverse
from  blogapp.models import Sort,Tages,Article,Comment,Contact,User
from django.core.paginator import Paginator
import re
from django.contrib.auth import authenticate,login,logout

def page_rang(page_id,article_list,num):
    '''生成页码列表'''
    paginator = Paginator(article_list,num)
    page_num = paginator.num_pages
    page_list = paginator.page(page_id)
    if page_num <= 5:
        page_num_list = paginator.page_range
    elif page_id <= 2:
        page_num_list = range(1, 6)
    elif page_num - page_id <= 2:
        page_num_list = range(page_num - 4, page_num + 1)
    else:
        page_num_list = (page_id - 2, page_id + 2)
    return page_num_list,page_list
# Create your views here.
class IndexView(View):
    def get(self,request):
        #查询
        article_list = Article.objects.all().order_by('-create_time')
        article_list_1 = Article.objects.all().order_by('-create_time')[0:2]
        sort = Sort.objects.all().order_by('-create_time')
        tages = Tages.objects.all().order_by('-create_time')
        page_num_list,page_list =page_rang(1,article_list,3)
        # for aritcle in article_list:
        #     comment_list = Comment.objects.filter(comment=aritcle)
        #     count = comment_list.count()
        #     aritcle.comment_count=count
        #     aritcle.save()
        #组织上下文
        context={
            'sorts':sort,
            'tages':tages,
            'article_list_1':article_list_1,
            'page_list':page_list,
            'page_num_list':page_num_list
        }



        return render(request,'index.html',context)

class PaginatorView(View):
    def get(self,request,page_id):
        article_list = Article.objects.all().order_by('-create_time')
        sort = Sort.objects.all().order_by('-create_time')
        tages = Tages.objects.all().order_by('-create_time')
        article_list_1 = Article.objects.all().order_by('-create_time')[0:2]
        page_num_list, page_list = page_rang(page_id, article_list, 3)

        context = {
            'sorts': sort,
            'tages': tages,
            'article_list_1': article_list_1,
            'page_list': page_list,
            'page_num_list': page_num_list
        }
        return  render(request ,'index_paginator1.html',context)



class AritcleDetail(View):
    '''文章详情页'''
    def get(self,request,article_id):
        try:
            aritcle = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return render(request,'404.html')
        article_list = Article.objects.all().order_by('-create_time')[0:2]
        comment_list = Comment.objects.filter(comment=aritcle)
        count = comment_list.count()
        print(count)
        aritcle.view_count+=1
        aritcle.save()
        comment = Comment.objects.filter(comment=aritcle)
        return render(request, 'detail.html', {'aritcle':aritcle,'article_list':article_list,'comment':comment,'count':count})



class AritcleComment(View):
    def post(self,request):
        user =request.user
        comment = request.POST.get('content')
        article_id=request.POST.get('article_id')
        article = Article.objects.get(id=article_id)
        # match=re.match('', comment)
        if not comment  :
           return JsonResponse({'errmsg':'请填写评论'})
        # elif match:
        #     return JsonResponse({'errmsg': '请不要发送空白评论'})
        comment_list = Comment.objects.filter(comment=article)
        Comment.objects.create(
            user=user.username,
            content=comment,
            comment=article,
            emil=user.email,
            web='www.baidu.com'

        )
        article.comment_count+=1
        article.save()
        return JsonResponse({ 'errmsg': '评论成功'})
        # user_name = request.GET.get('name')
        # comment = request.GET.get('comment')
        # print(comment)
        #
        # if not all([user_name,comment]):
        #     return redirect('404.html')
        # article = Article.objects.get(id =article_id)
        # print(article)
        # comment_list = Comment.objects.filter(comment=article)
        # Comment.objects.create(
        #     user=user_name,
        #     content=comment,
        #     comment=article
        #
        # )
        # context={
        # 'comment':comment_list,
        # 'aritcle':article
        # }
        #
        # return  render(request,'single.html',context)

class AllAritcleView(View):
    '''所有文章页'''
    def get(self,request,page_id):
        article_list = Article.objects.all()
        page_num_list, page_list = page_rang(page_id, article_list, 3)
        return render(request,'full-width.html',{'page_list':page_list,'page_num_list':page_num_list})


class All_Sort_AritcleView(View):
    '''所有分类文章详情页'''
    def get(self,request,page_id):
        sort_id =request.GET.get('sort')
        sort = Sort.objects.get(id=int(sort_id))
        article_list = Article.objects.filter(sort=sort)
        page_num_list, page_list = page_rang(page_id, article_list, 1)
        return render(request,'sort_full-width.html',{'page_list':page_list,'page_num_list':page_num_list,'sort':sort_id})


class All_Tage_AritcleView(View):
    '''所有标签分类文章详情页'''
    def get(self,request,page_id):
        tage_id = request.GET.get('tage')
        tage = Tages.objects.get(id=tage_id)
        article_list = Article.objects.filter(tages=tage)
        page_num_list, page_list = page_rang(page_id, article_list, 1)
        return render(request,'tags_full-width.html',{'page_list':page_list,'page_num_list':page_num_list,'tage':tage_id})


class AboutView(View):
    def get(self,request):
        return render(request,'about.html')


class ContactView(View):
    def post(self,request):
        user_name = request.POST.get('username')
        email = request.POST.get('email')
        suject = request.POST.get('subject')
        content = request.POST.get('text')
        if not all([user_name,email,suject,content]):
            return JsonResponse({'errmsg':'信息不完整'})
        Contact.objects.create(
            user=user_name,
            emil=email,
            subject=suject,
            content=content
        )
        return JsonResponse({'errmsg': '留言成功'})
    def get(self,request):
        return render(request,'contact.html')


class LoginView(View):
    def get(self,request):
        user = request.user
        if user.is_authenticated():
            return redirect(reverse('blog:index'))
        return  render(request,'login.html')

    def post(self, request):
        # 接受数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        # 校验数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '信息不完整'})
        user = authenticate(username=username, password=password)
        if user is not None :
            login(request,user)
            return redirect(reverse('blog:index'))
        else:
            return render(request,'login.html',{'errmsg':'用户名密码错误'})


class LoginOutView(View):
       '''退出登录'''
       def get(self,request):
          '''退出登录'''
          logout(request)
          return redirect(reverse('blog:login'))



class RegisiteView(View):
    def get(self,request):
        return  render(request,'regesite.html')
    '''注册校验 '''
    def post(self,request):
        #接收数据
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        #校验数据
        if not all([username, password, email]):
            # 数据不完整
            return render(request, 'regesite.html', {'errmsg': '数据不完整'})

            # 校验邮箱
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'regesite.html', {'errmsg': '邮箱格式不正确'})

        if allow != 'on':
            return render(request, 'regesite.html', {'errmsg': '请同意协议'})

            # 校验用户名是否重复
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 用户名不存在
            user = None

        if user:
            # 用户名已存在
            return render(request, 'regesite.html', {'errmsg': '用户名已存在'})
        user = User.objects.create_user(username, email, password)
        user.is_active = 1
        user.save()
        #发送数据
        return  redirect(reverse('blog:index'))


class UserInfoView(View):
    def get(self,request):
        '''用户中心'''
        return render(request,'userinfo.html')
