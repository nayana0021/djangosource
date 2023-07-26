from django.shortcuts import render, redirect
from .forms import UserForm

# 장고에서 제공하는 User 생성폼과 모델 가져오기
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 로그인 처리
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, "index.html")


def user_main(request):
    return render(request, "users/main.html")


# def signup(request):
#     """
#     회원가입 시 UserCreationForm(아이디,비밀번호,비밀번호 확인) 사용 방식
#     """
#     if request.method == "POST":
#         form = UserCreationForm(
#             request.POST
#         )  # 입력한걸 post 로 보내 / UserCreationForm 장고가 제공해주는 폼
#         if form.is_valid():  # 유효성검증
#             form.save()  # 통과하면 db 저장
#             return redirect("users:login")  # 이동할 페이지
#     else:
#         form = UserCreationForm()  # instance= 이 있다면 바인딩된 폼

#     return render(request, "users/register.html", {"form": form})


def signup(request):
    """
    회원가입 시 UserForm 사용 방식
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
    else:
        form = UserForm()

    return render(request, "users/register.html", {"form": form})


def common_login(request):
    if request.method == "POST":
        # 사용자 입력값 가져오기
        username = request.POST["username"]
        password = request.POST["password"]
        # 사용자가 존재한다면 권한을 가진 user 객체를 리턴해줌 : authenticate() 함수 역할임
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 세션에 정보가 담기게 됨
            login(request, user)
            return redirect("index")  # 로그인 되면 index로 가라

    return render(request, "users/login.html")


def common_logout(request):
    logout(request)  # 세션을 해제해줌
    return redirect("index")
