from django.shortcuts import render,redirect
from django.http import HttpResponse
import time
from .models import LunBo
from .forms import PhotoForm
# Create your views here.

def upload_image(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            #判断是否上传了文件

            if 'docfile' in request.FILES:
                image = request.FILES["docfile"]

                #修改文件名字
                image.name = str(request.user)+str(time)+'.jpg'

                s = LunBo()
                s.name = form.cleaned_data["name"]
                s.owner = request.user
                s.description = form.cleaned_data["description"]
                s.image = form.cleaned_data["image"]
                s.save()
                return HttpResponse('上传成功')
            else:
                #没有上传文件直接点了上传就重定向到上传页面
                return redirect('lunbo/upload_img.html')
        else:

            image = None
            return HttpResponse('上传失败')
    else:
        return render(request,'lunbo/upload_img.html')

