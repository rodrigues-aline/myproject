from core.models import User, Question, Answer, QuestionAnswered
from datetime import datetime


def user_jon():
    ze = User.objects.create_user(
        username='jon',
        first_name='Jon',
        last_name='Snow',
        email='jon@example.com',
        password='snow',
    )
    return ze


def questions_answers():
    q1 = Question.objects.create(question='Qual é o seu genero?')
    q2 = Question.objects.create(question='O Sr(a) apóia o controle nacional do petróleo do pré-sal?')

    answers = (Answer(question_id=q1, answer='Masculino'), Answer(question_id=q1, answer='Feminino'), Answer(question_id=q1, answer='Outro'),
               Answer(question_id=q2, answer='Sim'), Answer(question_id=q2, answer='Não'), Answer(question_id=q2, answer='Indiferente'))
    Answer.objects.bulk_create(answers)


def dashboard():
    answers = (QuestionAnswered(age=0, latitude=0, longitude=0, created_at=datetime.now(),
                                questions="{1: {'answer': 1}, 2: {'answer': 5}, 3: {'answer': 9}, 4: {'answer': 10}, 5: {'answer': 13}}"),
               QuestionAnswered(age=0, latitude=0, longitude=0, created_at=datetime.now(),
                                questions={1: {'answer': 1}, 2: {'answer': 5}, 3: {'answer': 9}, 4: {'answer': 10},
                                           5: {'answer': 13}}),
               QuestionAnswered(age=0, latitude=0, longitude=0, created_at=datetime.now(),
                                questions={1: {'answer': 1}, 2: {'answer': 5}, 3: {'answer': 9}, 4: {'answer': 10},
                                           5: {'answer': 13}}),
               QuestionAnswered(age=0, latitude=0, longitude=0, created_at=datetime.now(),
                                questions={1: {'answer': 1}, 2: {'answer': 5}, 3: {'answer': 9}, 4: {'answer': 10},
                                           5: {'answer': 13}}),
               QuestionAnswered(age=0, latitude=0, longitude=0, created_at=datetime.now(),
                                questions={1: {'answer': 1}, 2: {'answer': 5}, 3: {'answer': 9}, 4: {'answer': 10},
                                           5: {'answer': 13}}),
               QuestionAnswered(age=0, latitude=0, longitude=0, created_at=datetime.now(),
                                questions={1: {'answer': 1}, 2: {'answer': 5}, 3: {'answer': 9}, 4: {'answer': 10},
                                           5: {'answer': 13}})
               )
    QuestionAnswered.objects.bulk_create(answers)
