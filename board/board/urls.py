from django.urls import path
from .views import index, question_detail, answer_create, question_create

app_name = "board"

urlpatterns = [
    # http://127.0.0.1:8000/board/
    path("", index, name="index"),
    # http://127.0.0.1:8000/board/1/ 상세조회
    path("<int:qid>/", question_detail, name="detail"),
    # http://127.0.0.1:8000/board/create/ 질문등록
    path("create/", question_create, name="question_create"),
    # 답변
    # http://127.0.0.1:8000/board/answer/create/질문번호/
    path("answer/create/<int:qid>/", answer_create, name="answer_create"),
]
