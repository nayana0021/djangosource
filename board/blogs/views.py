from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse


def post_list(request):
    """
    Post 모델(테이블) 모두 가져오기 : 최신순
    """
    posts = Post.objects.order_by("-created_at")
    return render(request, "blogs/post_list.html", {"posts": posts})


@login_required(login_url="users:login")
def post_create(request):
    if request.method == "POST":
        # request.FILES : file 정보 따로 가져오기( 폼으로 가져올 수 없다 : post로..)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # user 정보가 없음 일단 False
            post.author = request.user
            post.save()
            return redirect("blog:post_list")
    else:
        form = PostForm()
    return render(request, "blogs/post_write.html", {"form": form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 좋아요 여부
    is_liked = False
    # 로그인 사용자가 게시물에 좋아요 표시를 했다면
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    context = {"post": post, "is_liked": is_liked}

    return render(request, "blogs/post_detail.html", context)


@login_required(login_url="users:login")
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:post_detail", post.id)
    else:
        form = PostForm(instance=post)

    return render(request, "blogs/post_edit.html", {"form": form})


@login_required(login_url="users:login")
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect("blog:post_list")


# 좋아요
@login_required(login_url="users:login")
def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 게시물에 대해 로그인 사용자가 누른 좋아요가 있는지 확인
    is_liked = post.likes.filter(id=request.user.id).exists()

    is_liked_change = False
    # 좋아요를 누른게 있다면 삭제
    if is_liked:
        post.likes.remove(request.user)
    # 좋아요를 추가
    else:
        post.likes.add(request.user)
        is_liked_change = True
    return JsonResponse({"likes": post.likes.count(), "is_liked": is_liked_change})
