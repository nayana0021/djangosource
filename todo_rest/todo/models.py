from django.db import models


class Todo(models.Model):
    """
    제목 : text => CharField or textField
    설명 : text => TextField
    작성날짜 : 시간/날짜
    완료여부 : True/False
    중요여부 : True/False
    """

    title = models.CharField(max_length=50)
    description = models.TextField()
    # DatetimeField 옵션
    # auto_now_add : 첫 입력 시 날짜/시간으로 세팅됨(insert)
    # auto_now : 수정할 때 마다 날짜/시간 변경이 일어남(update)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
