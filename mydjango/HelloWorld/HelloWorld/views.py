from django.http import HttpResponse
from django.shortcuts import render


def runoob(request):
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    views_for = {"name": "菜鸟教程",
                 "gender": "nan"}
    name="Bean"
    # 返回runoob的views_str、views_for、name参数
    return render(request, "runoob.html", {"views_str": views_str,
                                           "views_for":views_for ,
                                           "name":name})

# def hello(request):
#     return HttpResponse("Hello world ! ")
