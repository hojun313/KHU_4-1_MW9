print("--- blog/urls.py 파일 로드 시작 ---")
from django.urls import path
from . import views

urlpatterns = [
  path('', views.post_list, name='post_list'),
]