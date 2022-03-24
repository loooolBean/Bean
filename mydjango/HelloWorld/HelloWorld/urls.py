from django.urls import path
from . import views, testdb, search, searches
from django.conf.urls import url
from django.contrib import admin

# 拼接url地址,文件名.函数名

urlpatterns = [
    path('login/', views.login),
    path('add_emp/', views.add_emp),
    path('add_book/', views.add_book),
    url('admin/', admin.site.urls),  # 管理工具
    path('runoob/', views.runoob),
    path('testdb/', testdb.testdb),
    path('search-form/', search.search_form),
    path('search/', search.search),
    path('search-post/', searches.search_post),
]
