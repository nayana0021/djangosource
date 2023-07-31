from django.urls import path
from .views.base_views import index, question_detail
from .views.question_views import (
    question_create,
    question_edit,
    question_delete,
    vote_question,
)
from .views.answer_views import answer_create, answer_edit, answer_delete, vote_answer
from .views.comment_views import (
    comment_create_quesiton,
    comment_edit_quesiton,
    comment_delete_quesiton,
    comment_create_answer,
    comment_edit_answer,
    comment_delete_answer,
)

app_name = "board"

urlpatterns = [
    # http://127.0.0.1:8000/board/
    path("", index, name="index"),
    # http://127.0.0.1:8000/board/1/ 상세조회
    path("<int:qid>/", question_detail, name="detail"),
    # http://127.0.0.1:8000/board/question/create/ 질문등록
    path("question/create/", question_create, name="question_create"),
    # http://127.0.0.1:8000/board/question/modify/1/ 질문수정
    path("question/modify/<int:qid>/", question_edit, name="question_modify"),
    # http://127.0.0.1:8000/board/question/delete/1/ 질문삭제
    path("question/delete/<int:qid>/", question_delete, name="question_delete"),
    # 답변
    # http://127.0.0.1:8000/board/answer/create/질문번호/
    path("answer/create/<int:qid>/", answer_create, name="answer_create"),
    # http://127.0.0.1:8000/board/answer/modify/답변번호/
    path("answer/modify/<int:aid>/", answer_edit, name="answer_modify"),
    # http://127.0.0.1:8000/board/answer/delete/답변번호/
    path("answer/delete/<int:aid>/", answer_delete, name="answer_delete"),
    # 질문 댓글
    # 질문 댓글 추가
    path(
        "comment/create/question/<int:qid>/",
        comment_create_quesiton,
        name="comment_create_question",
    ),
    # 질문 댓글 수정
    path(
        "comment/edit/question/<int:comment_id>/",
        comment_edit_quesiton,
        name="comment_edit_question",
    ),
    # 질문 댓글 삭제
    path(
        "comment/delete/question/<int:comment_id>/",
        comment_delete_quesiton,
        name="comment_delete_question",
    ),
    # 답변 댓글
    # 답변 댓글 추가
    path(
        "comment/create/answer/<int:aid>/",
        comment_create_answer,
        name="comment_create_answer",
    ),
    # 답변 댓글 수정
    path(
        "comment/edit/answer/<int:comment_id>/",
        comment_edit_answer,
        name="comment_edit_answer",
    ),
    # 답변 댓글 삭제
    path(
        "comment/delete/answer/<int:comment_id>/",
        comment_delete_answer,
        name="comment_delete_answer",
    ),
    # 추천
    # 질문 추천
    path("vote/question/<int:qid>/", vote_question, name="vote_question"),
    # 답변 추천
    path("vote/answer/<int:aid>/", vote_answer, name="vote_answer"),
]
