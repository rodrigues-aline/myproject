from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from json import dumps


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser", on_delete=models.SET_NULL)
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Question(models.Model):
    question = models.CharField(max_length=512)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.question

    def to_dict_json(self):
        return {
            'id': self.id,
            'question': self.question,
        }


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=512)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.answer

    def to_dict_json(self):
        return {
            'id': self.id,
            'question_id': self.question_id.id,
            'answer': self.answer,
        }


class QuestionAnswered(models.Model):
    age = models.IntegerField(null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    questions = JSONField()
    created_at = models.DateTimeField()

    def to_dict_json(self):
        return {
            'id': self.id,
            'age': self.age,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'questions': self.questions,
            'created_at': self.created_at.isoformat(),
        }




