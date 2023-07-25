from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm


def todo_list(request):
    # 전체목록 가져오기
    # todos = Todo.objects.all()

    # 미완료된 목록 가져오기 (where절 이라고 생각하면 됨)
    # where complete = 0
    todos = Todo.objects.filter(complete=False)

    # templates/todo/todo_list.html -> templates 폴더는 자동으로 인식을 해서 그 밑에 것만 입력해준다
    return render(
        request, "todo/todo_list.html", {"todos": todos}
    )  # todo_list.html 에 입력함 (for 문에서 사용)


def todo_detail(request, id):
    # id 와 일치하는 todo 조회 후 보내기

    todo = get_object_or_404(Todo, id=id)

    return render(request, "todo/todo_detail.html", {"todo": todo})


def todo_create(request):
    """
    get/post 둘 다 동작
    """
    if request.method == "POST":
        form = TodoForm(request.POST)  #  DTO개념 : post로 넘어오는 값 담아서 form에 담음
        if form.is_valid():  # 유효성 검증(테이블 작성 기준)       (폼을 사용하면 유효성 검증이 쉽다)
            todo = form.save()  #  db반영 인서트 객체를 돌려줌 -> 담아서 쓴다
            return redirect("todo_detail", id=todo.id)
    else:
        # 화면단에서 사용 가능함 - 근데 안 예쁘다고..
        form = TodoForm()

    return render(request, "todo/todo_create.html", {"form": form})


def todo_edit(request, id):
    # id와 일치하는 todo 찾기
    todo = get_object_or_404(Todo, id=id)

    # post - 바인딩 된 폼에 post 요청으로 넘어오는 값 담기
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect("todo_detail", id=todo.id)
    else:
        # get - 찾은 todo를 폼에 바인딩 한 후 보내기 (연결시킨다는 얘기)
        form = TodoForm(instance=todo)
    return render(request, "todo/todo_edit.html", {"form": form})


def todo_done(request, id):
    """
    set complete=1
    """
    # 수정할 todo 찾기
    # todo = get_object_or_404(Todo, id=id)
    todo = Todo.objects.get(id=id)
    # 수정할 todo 값 변경
    todo.complete = True
    todo.save()
    return redirect("todo_list")


def done_list(request):
    # 완료된 목록 가져오기
    # where complete = 1
    dones = Todo.objects.filter(complete=True)

    return render(request, "todo/done_list.html", {"dones": dones})
