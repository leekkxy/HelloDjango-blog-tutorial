from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Tag,Category

# Create your views here.


def index(request):
    # return HttpResponse('欢迎访问！这里是/blog/views/index函数。我是lk，再见！')
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,template_name='blog/index.html',context={
        'Title':'这是主页',
        'Welcome':'欢迎来访！这是第二个版本了。用的render函数。',
        'post_list':post_list,
    })