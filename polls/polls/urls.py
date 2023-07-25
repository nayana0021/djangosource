from django.urls import path
from .views import index, detail, results, vote  # 이름만 사용

# from . import views -> 뷰스라는 모델을 임포트해서 views.index 이런식으로 사용

urlpatterns = [
    # 전체 질문목록 보여주기
    # http://127.0.0.1:8000/polls/
    path("", index, name="index"),
    # 특정 질문 조회
    # http://127.0.0.1:8000/polls/1
    path("<int:question_id>/", detail, name="detail"),
    # 투표 결과 보여주기
    # http://127.0.0.1:8000/polls/1/results/
    path("<int:question_id>/results/", results, name="results"),
    # 투표하기
    # http://127.0.0.1:8000/polls/1/vote/
    path("<int:question_id>/vote/", vote, name="vote"),
]
