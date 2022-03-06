from django.db import models
# 创建表格结构相当于，views调用表，urls通过路径再调用views的函数
from django.core.exceptions import ValidationError
from django import forms


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


class EmpForm(forms.Form):
    # CharField相当于char
    name = forms.CharField(min_length=4, label="姓名", error_messages={"min_length": "你太短了", "required": "该字段不能为空!"})
    # IntegerField相当于年龄
    age = forms.IntegerField(label="年龄")
    # DecimalField相当于工资
    salary = forms.DecimalField(label="工资")
    r_salary = forms.DecimalField(max_digits=5, decimal_places=2, label="请再输入工资")

    def clean_name(self):  # 局部钩子
        val = self.cleaned_data.get('name')
        if val.isdigit():
            raise ValidationError("用户名不能是纯数字")
        # elif models.Emp.objects.filter(name=val):
        #     raise ValidationError('用户名已存在')
        else:
            return val

    def clean(self):  # 全局钩子 确认两次输入的工资是否一致
        val = self.cleaned_data.get('salary')
        r_val = self.cleaned_data.get('r_salary')
        if val == r_val:
            return self.cleaned_data
        else:
            raise ValidationError("请确认工资是否一致。")
