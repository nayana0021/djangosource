from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from ..models import Question, Answer, Comment
from ..forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


####################### 질문 댓글
@login_required(login_url="users:login")
def comment_create_quesiton(request, qid):
    """
    질문 댓글 추가 - question id 가 필요함
    """
    # 질문 찾기
    question = get_object_or_404(Question, id=qid)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # form 안에는 user,question 정보가 없음 - db에 반영하면 안됨
            comment.author = request.user
            comment.question = question
            comment.save()
            # return redirect("board:detail", qid=qid)
            # name 앵커 이용
            return redirect(
                "{}#comment_{}".format(resolve_url("board:detail", qid=qid), comment.id)
            )
    else:
        form = CommentForm()

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_edit_quesiton(request, comment_id):
    """
    댓글 수정 - 댓글 id
    """
    # 댓글 하나 가져오기
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)  # modified_at 추가
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("board:detail", qid=comment.question.id)
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:detail", qid=comment.question.id), comment.id
                )
            )
    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_delete_quesiton(request, comment_id):
    """
    댓글 삭제 - 댓글 id
    """
    # 댓글 하나 가져오기
    comment = get_object_or_404(Comment, id=comment_id)

    # 댓글 삭제
    comment.delete()

    # detail 로 이동
    return redirect("board:detail", qid=comment.question.id)


####################### 답변 댓글
@login_required(login_url="users:login")
def comment_create_answer(request, aid):
    """
    답변 댓글 추가
    """
    answer = get_object_or_404(Answer, id=aid)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # 작성자, 답변번호가 없음
            comment.author = request.user
            comment.answer = answer
            comment.save()
            # return redirect("board:detail", qid=answer.question.id)
            # name 앵커 이용
            return redirect(
                "{}#comment_{}".format(
                    resolve_url("board:detail", qid=answer.question.id), comment.id
                )
            )
    else:
        form = CommentForm()

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_edit_answer(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)  # modified_at 추가
            comment.modified_at = timezone.now()
            comment.save()
            # return redirect("board:detail", qid=comment.answer.question.id)
            return redirect(
                "{}#comment{}".format(
                    resolve_url("board:detail", qid=comment.answer.question.id),
                    comment.id,
                )
            )
    else:
        form = CommentForm(instance=comment)
    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="users:login")
def comment_delete_answer(request, comment_id):
    """
    댓글 찾은 후 삭제 => detail 이동
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    # question 의 id 값 없는 상태 : 답변 댓글이기 때문에
    # answer 를 통해 question 값 어덩와야 함
    return redirect("board:detail", qid=comment.answer.question.id)
