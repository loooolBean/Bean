from django.urls import path
from . import views, testdb, search,searches

# 拼接url地址,文件名.函数名
urlpatterns = [
    path('runoob/', views.runoob),
    path('testdb/', testdb.testdb),
    path('search-form/', search.search_form),
    path('search/', search.search),
    path('search-post/', searches.search_post),
]