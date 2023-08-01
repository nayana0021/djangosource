from django.shortcuts import render, get_object_or_404
from ..models import Question, QuestionCount

from django.core.paginator import Paginator

# 필터링 여러 개 조건 사용할 때 이용(유용함)
from django.db.models import Q, Count

from tools.utils import get_client_ip


"""
페이지 나누기
Paginator 클래스
Paginator(전체리스트, 페이지당 보여줄개수)

has_previous : 이전 페이지 유무
has_next : 다음 페이지 유무

previous_page_number : 이전 페이지 번호
next_page_number : 다음 페이지 번호
number : 현재 페이지 번호
page_range : 페이지 범위
count : 전체 게시물 갯수
start_index : 현재 페이지 인덱스(1부터 시작)
페이지네이터 안에 들어있음~
"""


def index(request):
    # 질문 목록

    # 페이지 나누기 - 사용자가 요청한 페이지 가져오기
    # http://127.0.0.1:8000/board/?keyword=테스트&page=1&sort=recommend
    # page = request.GET['page']
    page = request.GET.get("page", 1)  # 페이지 값이 안 들어오면 1로 기본값을 줌
    keyword = request.GET.get("keyword", "")  # 기본 검색어는 없는 걸로 줌
    sort = request.GET.get("sort", "recent")  # 기본은 최신순

    # select * from question
    # question_list = Question.objects.all()

    # select * from question order by created_at desc
    if sort == "recommend":  # 추천순
        question_list = Question.objects.annotate(num_voter=Count("voter")).order_by(
            "-num_voter", "-created_at"
        )  # 앞에 - 붙으면 내림차순
    elif sort == "popular":  # 인기순
        question_list = Question.objects.annotate(num_answer=Count("answer")).order_by(
            "-num_answer", "-created_at"
        )
    else:  # 최신순
        question_list = Question.objects.order_by("-created_at")

    # 전체 질문 리스트에서 검색어를 기준으로 필터링 하기
    # 제목, 내용, 질문작성자, 답변작성자
    # __contains : 대소문자 구별, __icontains : 대소문자 구별없이
    if keyword:
        question_list = question_list.filter(
            Q(subject__icontains=keyword)
            | Q(content__icontains=keyword)
            | Q(author__username__icontains=keyword)
            | Q(answer__author__username__icontains=keyword)
        ).distinct()

    paginator = Paginator(question_list, 10)
    # paginator 사용자가 요청한 페이지 정보 담기
    page_obj = paginator.get_page(page)

    context = {
        "question_list": page_obj,
        "page": page,
        "keyword": keyword,
        "sort": sort,
    }

    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    page = request.GET.get("page")
    keyword = request.GET.get("keyword")
    sort = request.GET.get("sort")

    # qid 조회
    # select * from question where id=qid
    # get_object_or_404(), get(), filter()
    question = get_object_or_404(Question, id=qid)

    # 조회수 증가
    # client ip 가져오기
    ip = get_client_ip(request)

    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()

    if cnt == 0:
        # QuestionCount 테이블에 ip 와 question 추가
        qc = QuestionCount(ip=ip, question=question)
        qc.save()
        # Question 테이블에 조회수 증가
        if question.view_cnt:
            question.view_cnt += 1
        else:
            question.view_cnt = 1
        question.save()

    context = {
        "question": question,
        "page": page,
        "keyword": keyword,
        "sort": sort,
    }
    # 딕셔너리 구조기 때문에 여러개 담을 수 있다 (page, keyword 등...추가하려고)

    return render(request, "board/question_detail.html", context)
