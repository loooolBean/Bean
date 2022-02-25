from django.urls import path
from . import views, testdb

# 拼接url地址
urlpatterns = [
    path('runoob/', views.runoob),
    path('testdb/', testdb.testdb)
]