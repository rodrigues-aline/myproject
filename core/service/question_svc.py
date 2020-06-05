from core.models import Question, Answer, QuestionAnswered
from datetime import datetime


def add_answers(age, latitude, longitude, questions):
    QuestionAnswered.objects.create(age=0 if age == '' else age,
                                    latitude=0 if latitude == '' else latitude,
                                    longitude=0 if longitude == '' else longitude,
                                    questions=questions,
                                    created_at=datetime.now())


def list_questions():
    questions = Question.objects.all()
    return [q.to_dict_json() for q in questions]


def list_answers():
    answers = Answer.objects.select_related('question_id')
    return [a.to_dict_json() for a in answers]


def list_questions_answered():
    question_answered = QuestionAnswered.objects.all()
    return [qa.to_dict_json() for qa in question_answered]
