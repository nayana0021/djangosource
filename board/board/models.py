from django.db import models
from django.contrib.auth.models import User


# Question 테이블
# 번호(자동생성),제목,내용,작성날짜,수정날짜
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 유저가 탈퇴하면 전부 삭제
    subject = models.CharField(max_length=200, verbose_name="제목")
    # subject 라는 컬럼명 말고 "제목"이라는 이름으로 보여줘 이 뜻임
    content = models.TextField(verbose_name="내용")
    # auto_now_add : insert 시 자동으로 시간/날짜 삽입
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)
    # 어드민을 통해서 질문을 등록하면 수정날짜도 생성날짜랑 같이 들어가지만 폼에서 입력한것은 수정날짜가 null 로 들어간다(auto_now_add=True 가 아니라서)

    def __str__(self) -> str:
        return self.subject


# Answer 테이블
# 번호(자동생성),외래키 제약,내용,작성날짜,수정날짜
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)
