from django import forms

# 장고에서 제공하는 User 생성폼과 모델 가져오기
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    """
    상속관계

    forms.ModelForm
    |
    BaseUserCreationForm : username, password, password2
    |
    UserCreationForm
    |
    UserForm : User 모든 필드 + 상속(username, password, password2 : BaseUserCreationForm 상속받은거)

    UserCreationForm 클래스를 상속받는 Form 정의
    """

    # 부모가 넘겨주는 email 은 필수 입력 요소가 아님
    # 필수 입력 요소로 만들기 위해 재정의
    email = forms.EmailField(label="이메일")
    # 이메일 필수항목입니다 화면에 뜨게됨 - 이메일을 필수항목으로 하기 위해 재정의 하는 것임 : 비밀번호 초기화 시 이메일 전송을 처리하기 위한 준비단계라고 생각하면됨

    class Meta:
        model = User
        # fields = "__all__" + 상속 : 현재 연결된 user 테이블의 모든 필드가 화면에 보여지게 됨 + 상속된 필드까지
        fields = ["username", "email"]  # + 상속(password, password2) / 필요한 필드만 지정한다고
