from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
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

# 数据库添加
# 方法一：模型类实例化对象
# def add_book(request):
#     book = models.Book(title='菜鸟教程', price=300, publish='菜鸟出版社', pub_date="2008-8-8")
#     book.save()
#     return HttpResponse("<p>数据添加成功！</p>")

# 方法二：通过ORM提供的objects提供的方法create来实现
# def add_book(request):
#     books = models.Book.objects.create(title='如来神掌', price=200, publish='菜鸟教程', pub_date='2008-08-08')
#     print(books, type(books))
#     return HttpResponse('<p>数据添加成功！</p>')


#  查找

# 使用all()方法查询
# def add_book(request):
#     books = models.Book.objects.all()
#     # print(books, type(books))
#     for i in books:
#         print(i.title)
#     return HttpResponse('<p>查找成功</p>')

# filter()方法用于查询符合条件的数据
# def add_book(request):
#     books = models.Book.objects.filter(pk=1)
#     print(books)
#     books = models.Book.objects.filter(publish='菜鸟出版社', price=300)
#     print(books, type(books))
#     return HttpResponse('<p>查找成功</p>')

# exclude()方法用于查询不符合条件的数据
# def add_book(request):
#     books = models.Book.objects.exclude(pk=1)
#     print(books)
#     print("============")
#     books = models.Book.objects.filter(publish='菜鸟出版社', price=300)
#     print(books, type(books))
#     return HttpResponse('<p>查找成功</p>')

# get() 方法用于查询符合条件的返回模型类的对象符合条件的对象只能为一个，如果符合筛选条件的对象超过了一个或者没有一个都会抛出错误。
# order_by() 方法用于对查询结果进行排序。参数的字段名要加引号;降序为在字段前面加个负号 -。
# def add_book(request):
#     books = models.Book.objects.order_by("price") # 查询所有，按照价格升序排列
#     books = models.Book.objects.order_by("-price")  # 查询所有，按照价格降序排列
#     return HttpResponse(books[3])

#  reverse() 方法用于对查询结果进行反转。
#  count() 方法用于查询数据的数量返回的数据是整数。
#  first() 方法返回第一条数据返回的数据是模型类的对象也可以用索引下标 [0]。
#  last() 方法返回最后一条数据返回的数据是模型类的对象不能用索引下标 [-1]，ORM 没有逆序索引。

# exists() 方法用于判断查询的结果 QuerySet 列表里是否有数据。
# 返回的数据类型是布尔，有为 true，没有为 false。
# 注意：判断的数据类型只能为 QuerySet 类型数据，不能为整型和模型类的对象。
def add_book(request):
    books = models.Book.objects
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为整型
    books = models.Book.objects.count()
    # 报错，判断的数据类型只能为QuerySet类型数据，不能为模型类对象
    books = models.Book.objects.first()
    return HttpResponse("<p>查找成功！</p>")