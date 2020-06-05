from django.contrib import admin

from core.models import ActivityLog, Question, Answer, QuestionAnswered


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'question_id')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
