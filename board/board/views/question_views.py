from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question
from ..forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


@login_required(login_url="users:login")
def question_create(request):
    """
    질문등록
    get - 비어있는 questionForm 보내기
    post - QuestionForm 에 사용자 입력값 연결
    """
    if request.method == "POST":
        # 사용자 입력값 가져오기
        # subject = request.POST["subject"]
        # content = request.POST["content"]
        # 유효성 검사 코드
        # Question = Question(subject=subject,content=content)
        # question.save()
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)  # 유저 정보가 없기 때문에 바로 커밋을 하지 않음
            question.author = request.user  # request.user : 로그인 사용자
            question.save()
            return redirect("board:index")

    else:
        form = QuestionForm()
    return render(request, "board/question_create.html", {"form": form})


@login_required(login_url="users:login")
def question_edit(request, qid):
    """
    get : 수정할 질문을 보여주기
          수정 질문 찾기 => form 에 질문 담아서 보내기
    post : 질문 수정
    """

    question = get_object_or_404(Question, id=qid)  # 수정 질문 찾기

    if request.method == "POST":
        # POST 로 넘어온 내용 폼이랑 연결해서 담아줘
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            # 수정날짜 추가
            question = form.save(commit=False)
            question.modified_at = timezone.now()
            question.save()
            return redirect("board:detail", qid=qid)

    else:
        form = QuestionForm(instance=question)  # 연결해서 담아서 보냄

    return render(request, "board/question_edit.html", {"form": form})


@login_required(login_url="users:login")
def question_delete(request, qid):
    """
    qid 로 질문찾기 => 삭제(delete())
    """
    question = get_object_or_404(Question, id=qid)
    question.delete()

    # 삭제 후 리스트 이동
    return redirect("index")


# 질문 추천
@login_required(login_url="users:login")
def vote_question(request, qid):
    # question 찾기
    question = get_object_or_404(Question, id=qid)

    # 로그인 사용자와 질문작성자가 동일할 때 본인이 작성할 글은 추천 불가 라는 메세지 보여주기
    if request.user == question.author:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.")
    else:
        # 추천 user 추가
        question.voter.add(request.user)
    # detail 이동
    return redirect("board:detail", qid=qid)
