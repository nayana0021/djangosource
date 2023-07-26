from django.shortcuts import render, get_object_or_404, redirect
from .models import Question


def index(request):
    """
    전체 질문목록 가져오기 - 작성날짜 내림차순
    """
    question_list = Question.objects.order_by("-pub_date")
    return render(request, "polls/index.html", {"question_list": question_list})


def detail(request, question_id):
    # question_id 를 이용해서 선택사항 가져오기 => Question 을 찾으면
    # Question 과 관련된 Choice 는 알아서 따라감
    question = get_object_or_404(Question, id=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    # 투표수 증가

    # 질문 가져오기
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        try:
            # question 의 id를 이용해서 Choice 찾기
            selected_choice = question.choice_set.get(id=request.POST["choice"])
        except KeyError as e:
            return render(request, "polls/detail.html")
        else:
            selected_choice.vote += 1
            selected_choice.save()
            # 투표 성공 후 결과 페이지로 이동
            return redirect("results", question_id=question_id)
