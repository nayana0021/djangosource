from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserForm(UserCreationForm):
    """
    UserCreationForm 은 username(id), password1, password2 만 들어있음
    다른 정보를 받기 원한다면 추가 후 필요 ==> 새로운 클래스 작성
    """

    # 부모가 내려줄때 email 은 null 이 가능한 상태로 상속 됨 => required 상태로 사용하기 위해서 선언(재선언)
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        # 모델(테이블)에서 사용할 필드 지정
        fields = ["username", "email"]
