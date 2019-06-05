from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import RegisterForm # 注册用户
from .models import ArticleTable,CategoryTable
from comments.forms import CommentForm

from django.views.generic import ListView
from django.db.models import aggregates,Avg
# Create your views here.

# 首页
# def index(request):
#     article_list = ArticleTable.objects.all().order_by('-created_time')
#     return render(request,'website/index.html',context={
#         'article_list':article_list,
#     })
class IndexView(ListView):
    model = ArticleTable
    template_name = 'website/index.html'
    context_object_name = 'article_list'

    paginate_by =1 # 一页10篇文章


# 分类
class CategoryView(ListView):
    model = ArticleTable
    template_name = 'website/index.html'
    context_object_name = 'article_list'
    def get_queryset(self):
        cate = get_object_or_404(CategoryTable,pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(article_category=cate)

# 用户注册
def register(request):
    if request.method == 'POST': # 判断是否是post请求
        form = RegisterForm(request.POST)
        # 验证数据合法性
        if form.is_valid():
            form.save()
            return redirect('/')# 返回首页
    else:
        form = RegisterForm()
    return render(request,'website/register.html',context={'form':form})


# 关于我们
def about(request):
    return render(request,'website/about.html')

# 联系我们
def contact(request):
    return render(request,'website/contact.html')

# 个人中心
def person(request):
    return render(request,'website/person.html')


# 详情页
def detail(request,pk):
    post = get_object_or_404(ArticleTable, pk=pk)
    post.increase_views()
    form = CommentForm()
    comment_list = post.comment_set.all()
    comment_count = post.comment_set.filter(post_id=pk).count() # 评论数量
    avg_grade = post.comment_set.filter(post_id=pk).aggregate(Avg('score')) # 平均评分
    ArticleTable.objects.filter(id=pk).update(comment_count=comment_count)
    ArticleTable.objects.filter(id=pk).update(avg_grade=avg_grade['score__avg'])
    context =  {
                'post':post,
                'form':form,
                'comment_list':comment_list,
                'comment_count':comment_count
    }
    return render(request,'website/detail.html',context=context)



# 归档
def archives(request,year,month):
    article_list = ArticleTable.objects.filter(created_time__year=year,
                                               created_time__month=month,
                                               ).order_by('-created_time')
    return render(request,'website/index.html',context={'article_list':article_list})