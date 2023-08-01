from django.db import models
from django.contrib.auth.models import User

# Question, Answer 모델에서 author, voter 두 개의 필드가 User 모델 참조
# user.question_set 이렇게 Question 모델에 접근할 때 어느 필드가 기준이냐? 를 알려줘야 함
# 특정 필드에 이름만 부여 해놓기 : related_name

# ManyToMany
# User.question_set' for 'board.Question.author - 에러 메시지 어느 테이블로 접근해야하는지 모르는 상황이라는 뜻임


# Question 테이블
# 번호(자동생성),제목,내용,작성날짜,수정날짜
class Question(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_question"
    )
    # 유저가 탈퇴하면 전부 삭제
    subject = models.CharField(max_length=200, verbose_name="제목")
    # subject 라는 컬럼명 말고 "제목"이라는 이름으로 보여줘 이 뜻임
    content = models.TextField(verbose_name="내용")
    # auto_now_add : insert 시 자동으로 시간/날짜 삽입
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)
    # 어드민을 통해서 질문을 등록하면 수정날짜도 생성날짜랑 같이 들어가지만 폼에서 입력한것은 수정날짜가 null 로 들어간다(auto_now_add=True 가 아니라서)
    # 추천 필드
    voter = models.ManyToManyField(User, related_name="voter_question")
    # 조회수
    view_cnt = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.subject


# Answer 테이블
# 번호(자동생성),외래키 제약,내용,작성날짜,수정날짜
class Answer(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_answer"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)
    # 추천 필드
    voter = models.ManyToManyField(User, related_name="voter_answer")


# 댓글 테이블
# 질문, 답변 댓글 모두 저장(하나의 테이블) ==> 구분은 어떻게 할 것인가?
# 번호(자동생성), 작성자, 댓글내용, 작성날짜, 수정날짜, 외래키(질문,답변 구분을 위해)
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="댓글내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    modified_at = models.DateTimeField(verbose_name="수정날짜", null=True, blank=True)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True, blank=True
    )
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)


class QuestionCount(models.Model):
    """
    조회수 업데이트를 위한 모델
    사용자의 ip 저장
    """

    ip = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ip
