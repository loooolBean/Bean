from django.db import models
# 创建表格结构相当于，views调用表，urls通过路径再调用views的函数

# Create your models here.
# class demo2(models.Model):
#     name = models.CharField(max_length=20)
#     id = models.CharField(max_length=20, primary_key=True)
# class Test(models.Model):
#     name = models.CharField(max_length=20)
class demo(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)


class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, )
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


# 以上是admin表格

# class Book(models.Model):
#     id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
#     title = models.CharField(max_length=32) # 书籍名称
#     price = models.DecimalField(max_digits=5, decimal_places=2) # 书籍价格
#     publish = models.CharField(max_length=32) # 出版社名称
#     pub_date = models.DateField() # 出版时间

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()