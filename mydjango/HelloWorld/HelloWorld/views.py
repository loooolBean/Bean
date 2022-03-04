from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from TestModel import models
from TestModel.My_Forms import EmpForm
from django import forms
from django.core.exceptions import ValidationError


def runoob(request):
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    views_for = {"name": "菜鸟教程",
                 "gender": "nan"}
    name = "Bean"
    # 返回runoob的views_str、views_for、name参数
    return render(request, "runoob.html", {"views_str": views_str,
                                           "views_for": views_for,
                                           "name": name})


# ========================================
# 数据库添加
# ========================================
# 方法一：模型类实例化对象
# def add_book(request):
# book = models.Book(title='菜鸟教程', price=300, publish='菜鸟出版社', pub_date="2008-8-8")
# book.save()

# 方法二：通过ORM提供的objects提供的方法create来实现
#     books = models.Book.objects.create(title='如来神掌', price=200, publish='菜鸟教程', pub_date='2008-08-08')
#     print(books, type(books))
#     return HttpResponse('<p>数据添加成功！</p>')

# ========================================
# 查找
# ========================================
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

# def add_book(request):
#     books = models.Book.objects
# 报错，判断的数据类型只能为QuerySet类型数据，不能为整型
# books = models.Book.objects.count()
# 报错，判断的数据类型只能为QuerySet类型数据，不能为模型类对象
# books = models.Book.objects.first()
# return HttpResponse("<p>查找成功！</p>")

# values() 方法用于查询部分字段的数据;values_list()方法用于查询部分字段的数据
# values() 返回的是 QuerySet 类型数据，类似于 list，里面不是模型类的对象，而是一个可迭代的字典序列，字典里的键是字段，值是数据;
# values_list()里面是一个个元组，元组里放的是查询字段对应的数据。
# 参数的字段名要加引号
# 想要字段名和数据用 values;只想要数据用values_list
# def add_book(request):
# 查询所有的id字段和price字段的数据
# books = models.Book.objects.values('pk', 'price')
# print('===================')
# print(books[0]['price'], type(books))  # 得到的是第一条记录的price字段的数据
# print(books)

# 查询所有的price字段和publish字段的数据
# books = models.Book.objects.values_list("pk", "publish")
# print('============')
# # print(books)
# print(books[0][0], type(books))  # 得到的是第一条记录的price字段的数据
# return HttpResponse("<p>查找成功</p>")

# distinct() 方法用于对数据进行去重。
# 查询一共有多少个出版社
# books = models.Book.objects.values_list("price").distinct()  # 对模型类的对象去重没有意义，因为每个对象都是一个不一样的存在。
# books = models.Book.objects.distinct()
# print(books)
# return HttpResponse("<p>查找成功！</p>")

# filter() 方法基于双下划线的模糊查询（exclude 同理）。
# 注意：filter 中运算符号只能使用等于号 = ，不能使用大于号 > ，小于号 < ，等等其他符号。
# __in 用于读取区间，= 号后面为列表 。
# 查询价格为200或者300的数据
# books = models.Book.objects.filter(price__in=[200, 300])
# print(books)
# __gt查询价格大于200的数据;__gte 大于等于，= 号后面为数字;__lt 小于;__lte;
# __range 在 ... 之间，左闭右闭区间，= 号后面为两个元素的列表。
# __contains 包含，= 号后面为字符串;__icontains 不区分大小写的包含，= 号后面为字符串;
# __startswith 以指定字符开头，= 号后面为字符串;__endswith 以指定字符结尾，= 号后面为字符串
# books = models.Book.objects.filter(price__gt=200)
# return HttpResponse("<p>查找成功！</p>")

# ========================================
# 删除
# ========================================
# 方式一：使用模型类的 对象.delete()，返回值：元组，第一个元素为受影响的行数。
# books=models.Book.objects.filter(pk=8).first().delete() #删除id=8的第一条数据

# 方式二：使用 QuerySet 类型数据.delete()(推荐)，返回值：元组，第一个元素为受影响的行数。
# books=models.Book.objects.filter(pk__in=[1,2]).delete()

# 注意：
#
# a. Django 删除数据时，会模仿 SQL约束 ON DELETE CASCADE 的行为，也就是删除一个对象时也会删除与它相关联的外键对象。
# b. delete() 方法是 QuerySet 数据类型的方法，但并不适用于 Manager 本身。也就是想要删除所有数据，不能不写 all。
# books=models.Book.objects.delete()　 # 报错
# books=models.Book.objects.all().delete()　　 # 删除成功

# ========================================
# 修改
# ========================================

# 方式一：
# 模型类的对象.属性 = 更改的属性值
# 模型类的对象.save()
# 返回值：编辑的模型类的对象。
# def add_book(request):
#     books = models.Book.objects.filter(pk=1).first()
#     books.price = 250
#     books.save()

# 方式二：QuerySet 类型数据.update(字段名=更改的数据)（推荐）
# 返回值：整数，受影响的行数
#     books = models.Book.objects.filter(pk__in=[1, 2]).update(price=888)
#     return HttpResponse(books)

# ==============================================================================
# 多表实例
# ==============================================================================

# 一对多(外键 ForeignKey)
# 方式一: 传对象的形式，返回值的数据类型是对象，书籍对象。
# def add_book(request):
#  获取出版社对象
# pub_obj = models.Publish.objects.filter(pk=1).first()
#  给书籍的出版社属性publish传出版社对象
# book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
# print(book, type(book))
# return HttpResponse(book)

# 方式二: 传对象 id 的形式(由于传过来的数据一般是 id,所以传对象 id 是常用的)。
# 一对多中，设置外键属性的类(多的表)中，MySQL 中显示的字段名是:外键属性名_id。
# 返回值的数据类型是对象，书籍对象。
#     #  获取出版社对象
#     pub_obj = models.Publish.objects.filter(pk=1).first()
#     #  获取出版社对象的id
#     pk = pub_obj.pk
#     #  给书籍的关联出版社字段 publish_id 传出版社对象的id
#     book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)
#     print(book, type(book))
#     return HttpResponse(book)

# 多对多：在第三张表上关联数据
# 方式一：传对象形式，无返回值
# def add_book(request):
# chong = models.Author.objects.filter(name='令狐冲').first()
# ying = models.Author.objects.filter(name='任盈盈').first()
# book = models.Book.objects.filter(title='菜鸟教程').first()
# book.authors.add(chong, ying)  # 给书籍对象的 authors 属性用 add 方法传作者对象
# return HttpResponse(book)

# 方式二：传对象id形式，无返回值
# chong = models.Author.objects.filter(name='令狐冲').first()
# pk = chong.pk
# book = models.Book.objects.filter(title='冲灵剑法').first()
# book.authors.add(pk)
# return HttpResponse('ok')

# 关联管理器(对象调用)
# 前提：多对多（双向均有关联管理器）;一对多(只有多的那个类的对象有关联管理器，即反向才有)
# 语法格式：
# 正向：属性名
# 反向：小写类名加 _set
# add()：用于多对多，把指定的模型对象添加到关联对象集（关系表）中。
# 注意：add() 在一对多(即外键)中，只能传对象（ *QuerySet数据类型），不能传 id（*[id表]）。
# *[ ] 的使用:

# def add_book(request):
#     book_obj = models.Book.objects.get(pk=3)
#     author_list = models.Author.objects.filter(id__gt=1)
#     book_obj.authors.add(*author_list) #  将id大于2的作者对象添加到这本书的坐着集合中
#     # 方式二：传对象 id
#     book_obj.authors.add(*[1, 3])  # 将 id=1 和 id=3 的作者对象添加到这本书的作者集合中
#     return HttpResponse('ok')

# create()：创建一个新的对象，并同时将它添加到关联对象集之中。
# remove()：从关联对象集中移除执行的模型对象。
# clear()：从关联对象集中移除一切对象，删除关联，不会删除对象。

# ===================================
# 跨表查询（ORM查询）
# ====================================
# 一对多
# 查询主键为3的书籍的出版社所在的城市(正向)
# def add_book(request):
    # book = models.Book.objects.filter(pk=3).first()
    # res = book.publish.city
    # print(res, type(res))
    # 查询明教出版社的书籍名（反向）
    # 反向：对象.小写类名_set() 可以跳转到关联的表（书籍表）
    # pub.book_set.all():取出书籍表中的所有书籍对象，在一个QuerySet里，遍历取出一个个书籍对象。
    #     pub=models.Publish.objects.filter(name='华山出版社').first()
    #     res = pub.book_set.all()
    #     for i in res:
    #         print(i.title)

    # 一对一
    # 正向：查询令狐冲的电话
    # author = models.Author.objects.filter(name='令狐冲').first()
    # res = author.au_detail.tel
    # print(res,type(res))

    # 查询所有住址在黑木崖的作者的姓名。
    # # 反向：一对一的反向，用 对象.小写类名 即可，不用加 _set。
    # addr = models.AuthorDetail.objects.filter(addr='黑木崖').first()
    # res = addr.author.name
    # print(res, type(res))
    # return HttpResponse('ok')

# 多对多
    # 正向:对象.属性(book.authors)可以跳转到关联的表(作者表)。
    # book = models.Book.objects.filter(title='菜鸟教程').first()
    # res = book.authors.all()
    # for i in res:
    #     print(i.name, i.au_detail.tel)
    #
    # # 反向：查询任我行出过的所有书籍的名字。
    # author = models.Author.objects.filter(name='任我行').first()
    # res = author.book_set.all()
    # for i in res:
    #     print(i.title)
    # return HttpResponse('ok')

# =============================================================
# 基于双下划线的跨表查询
# =============================================================
# 正向：属性名称__跨表的属性名称
# 反向：小写类名__跨表的属性名称
# 一对多：查询菜鸟出版社出版过的所有书籍的名字与价格

def add_book(request):
    # res1 = models.Book.objects.filter(publish__name="华山出版社").values_list('title', 'price')
    # res2 = models.Publish.objects.filter(name='华山出版社').values_list('book__title', 'book__price')
    # print(res1, type(res1), res2, type(res2))

# 多对多：查询任我行出版过的所有图书
# 正向：通过 属性名称__跨表的属性名称（authors__name）跨表获取数据
#     res = models.Book.objects.filter(authors__name="任我行").values_list('tittle')
# 反向：通过 小写类名__跨表的属性名称（book__tittle）跨表获取数据
#     res = models.Author.objects.filter(name="任我行").values_list("book__title")

# 一对一：查询任我行的手机号
# 正向：通过 属性名称__跨表的属性名称（au_detail_tell）跨表获取数据。
    res1 = models.Author.objects.filter(name='任我行').values_list("au_detail__tel")
# 反向：通过小写类名__跨表的属性名称（author__name）跨表获取数据
    res2 = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")
    print(res1, res2)
    return HttpResponse('ok')

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "add_emp.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():  # 进行数据校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            data.pop('r_salary')
            print(data)

            models.Emp.objects.create(**data)
            return HttpResponse(
                'ok'
            )
            # return render(request, "add_emp.html", {"form": form})
        else:
            print(form.errors)    # 打印错误信息
            clean_errors = form.errors.get("__all__")
            print(222, clean_errors)
        return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})