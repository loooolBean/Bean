from django.urls import path
from . import views

# 拼接url地址
urlpatterns = [
    path('runoob/', views.runoob),
]