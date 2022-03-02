from django.http import HttpResponse
from django.shortcuts import render
from TestModel import models


def runoob(request):
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    views_for = {"name": "菜鸟教程",
                 "gender": "nan"}
    name = "Bean"
    # 返回runoob的views_str、views_for、name参数
    return render(request, "runoob.html", {"views_str": views_str,
                                           "views_for": views_for,
                                           "name": name})


# def hello(request):
#     return HttpResponse("Hello world ! ")

# 方法一：模型类实例化对象
# def add_book(request):
#     book = models.Book(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8")
#     book.save()
#     return HttpResponse("<p>数据添加成功！</p>")

# 方法二：通过ORM提供的objects提供的方法create来实现（推荐）
def add_book(request):
    # book = models.Book(title="菜鸟教程",price=300,publish="菜鸟出版社",pub_date="2008-8-8")
    # book.save()
    # return HttpResponse("<p>数据添加成功！</p>")

    #  获取出版社对象
    pub_obj = models.Publish.objects.filter(pk=1).first()
    #  给书籍的出版社属性publish传出版社对象
    book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
    print(book, type(book))
    return HttpResponse(book)
