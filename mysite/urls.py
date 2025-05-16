print("--- mysite urls.py 파일이 로드되었습니다! ---")
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
