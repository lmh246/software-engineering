from django.shortcuts import render,get_object_or_404,redirect
from website.models import ArticleTable
from django.db.models import Count

from .models import Comment
from .forms import CommentForm

# Create your views here.

def post_comment(request,post_pk):
    post = get_object_or_404(ArticleTable,pk=post_pk) # 获取当前文章

    # 如果说post请求处理表单数据
    if request.method == 'POST':
        form = CommentForm(request.POST)

        # 判断数据是否有效
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('http://localhost:8000')
        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list,
                       }
            return render(request, 'website/detail.html', context=context)
    return redirect('http://localhost:8000')



