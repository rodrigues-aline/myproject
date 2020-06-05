from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json


class TestQuestionhApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.questions_answers()
        fixtures.dashboard()

    def test_question_api(self):
        client = Client()
        self._dashboard(client)
        self._list_question(client)
        self._add_answers(client)

    def _list_question(self, client):
        r = client.get('/api/list_questions')
        data = json.loads(r.content.decode('utf-8'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(type(list()), type(data['questions']))
        for k in ['id', 'question']:
            self.assertIsNotNone(data['questions'][0][k])
        self.assertEqual(type(list()), type(data['answers']))
        for k in ['id', 'question_id', 'answer']:
            self.assertIsNotNone(data['answers'][0][k])

    def _dashboard(self, client):
        r = client.get('/api/dashboard')
        data = json.loads(r.content.decode('utf-8'))
        self.assertEqual(200, r.status_code)
        self.assertEqual(type(list()), type(data['dashboard']))
        if len(data['dashboard']) > 0:
            for k in ['age', 'latitude', 'longitude', 'questions']:
                self.assertIsNotNone(data['dashboard'][0][k])

    def _add_answers(self, client):
        answers1 = {'age': '',
                   'latitude': '',
                   'longitude': '',
                   'questions': json.dumps({'1': {'answer': 1}, '2': {'answer': 5}, '3': {'answer': 9}, '4': {'answer': 11}, '5': {'answer': 13}})}
        answers2 = {'age': '',
                    'latitude': '',
                    'longitude': '',
                    'questions': json.dumps({'1': {'answer': 3}, '2': {'answer': 4}, '3': {'answer': 7}, '4': {'answer': 12}, '5': {'answer': 14}})}
        r1 = client.post('/api/add_answers', answers1)
        r2 = client.post('/api/add_answers', answers2)
        r3 = client.get('/api/dashboard')
        self.assertEqual({200}, {r.status_code for r in [r1, r2, r3]})
        answers = json.loads(r3.content.decode('utf-8'))
        self.assertEqual(8, len(answers['dashboard']))
