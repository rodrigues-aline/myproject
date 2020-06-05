# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, question_svc, globalsettings_svc
from django.views.decorators.csrf import csrf_exempt


def dapau(request):
    raise Exception('break on purpose')

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated:
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated else {'authenticated': False}
    return JsonResponse(i_am)


def settings(request):
    le_settings = globalsettings_svc.list_settings()
    return JsonResponse(le_settings)


def dashboard(request):
    questions = question_svc.list_questions()
    answers = question_svc.list_answers()
    dashboard = question_svc.list_questions_answered()
    return JsonResponse({'dashboard': dashboard, 'questions': questions, 'answers': answers})


def list_questions(request):
    questions = question_svc.list_questions()
    answers = question_svc.list_answers()
    return JsonResponse({'questions': questions, 'answers': answers})


def add_answers(request):
    age = request.POST['age']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    questions = json.loads(request.POST['questions'])
    question_svc.add_answers(age, latitude, longitude, questions)
    return JsonResponse({})


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d
