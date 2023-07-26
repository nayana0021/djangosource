from django.contrib import admin
from .models import Question, Choice

# 어드민 사이트에서 모델을 관리하기 가장 쉬운 방법 - 기본적으로 Question text 먼저 그 다음 날짜가 화면에 뜨게됨
# admin.site.register(Question)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields 에 정의한 순서대로 화면에 보여지게 됨 - 커스텀 개념이라고 생각하면 됨
    # fields = ["pub_date", "question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date")  # question text 와 날짜도 같이 뜸


admin.site.register(Question, QuestionAdmin)
