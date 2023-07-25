from django.db import models


# 설문 테이블
# 설문 내용, 설문작성날짜
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # str 을 넣으니 어드민 페이지에서 제목이 나오게 된다 객체상태인것을 보여달라고 하는 코드임
    def __str__(self) -> str:
        # toString() 자바의 투스트링과 같은 역할
        return self.question_text


# 선택 테이블 - 외래키 제약조건
# 설문 테이블, 선택 내용, 투표수
class Choice(models.Model):
    # 외래키 제약조건
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self) -> str:
        # toString()
        return self.choice_text
