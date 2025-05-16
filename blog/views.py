print("--- blog/views.py 파일 로드 시작 ---")
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    print("--- post_list view 함수 실행 시작 ---")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(f"--- View에서 가져온 게시글 수: {len(posts)} ---")
    print("--- render 함수 호출 직전 ---")
    return render(request, 'blog/post_list.html', {'posts': posts})
