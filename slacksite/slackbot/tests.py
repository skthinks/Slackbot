import json
import os

from django.test import TestCase
from django.utils.encoding import force_text
from models import User, OffenceLog

TOKEN = os.environ['WEBHOOK_TOKEN']


class SlackBotViewsTestCase(TestCase):
    def test_urls(self):
        resp = self.client.get('/slack/leaderboard/')
        self.assertEqual(resp.status_code, 400)
        resp = self.client.get('/slack/leaderboard/?q=weekly')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/slack/leaderboard/?x=weekly')
        self.assertEqual(resp.status_code, 400)
        resp = self.client.get('/slack/leaderboard/?q=monthly')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/slack/lead/?q=weekly')
        self.assertEqual(resp.status_code, 404)
        resp = self.client.get('/slack/leaderboard/?q=Daily')
        self.assertEqual(resp.status_code, 400)

    def test_post(self):
        resp = self.client.post('/slack/', {'token': TOKEN,
                                            'user_name': 'sk',
                                            'user_id': '123',
                                            'text': 'This is a test'})
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post('/slack/?q=1', {'token': TOKEN,
                                                'user_name': 'sk',
                                                'user_id': '123',
                                                'text': 'This is a test'})
        self.assertEqual(resp.status_code, 405)
        resp = self.client.post('/slack/', {'token': TOKEN,
                                            'user_name': '',
                                            'user_id': '',
                                            'text': ''})
        self.assertEqual(resp.status_code, 400)
        resp = self.client.post('/slack/', {'token': TOKEN,
                                            'user_name': 'Sk',
                                            'user_id': '456',
                                            'text': ''})
        self.assertEqual(resp.status_code, 200)
        resp = self.client.post('/slack/', {'token': TOKEN,
                                            'user_name': 'Sk2',
                                            'user_id': '',
                                            'text': ''})
        self.assertEqual(resp.status_code, 400)
        resp = self.client.post('/slack/', {'token': TOKEN,
                                            'user_name': '',
                                            'user_id': '12',
                                            'text': ''})
        self.assertEqual(resp.status_code, 400)
        resp = self.client.post('/slack/', {'token': TOKEN,
                                            'user_name': '',
                                            'user_id': '',
                                            'text': 'sadsa'})
        self.assertEqual(resp.status_code, 400)
        resp = self.client.post('/slack/', {'user_name': '',
                                            'user_id': '',
                                            'text': 'sadsa'})
        self.assertEqual(resp.status_code, 403)
        resp = self.client.post('/slack/', {'token': "1232421dnslafn",
                                            'user_name': '',
                                            'user_id': '',
                                            'text': 'sadsa'})
        self.assertEqual(resp.status_code, 403)

    def test_json_get(self):
        resp = self.client.get('/slack/leaderboard/?q=weekly')
        self.assertJSONEqual(force_text(resp.content), [])
        resp = self.client.get('/slack/leaderboard/?q=monthly')
        self.assertJSONEqual(force_text(resp.content), [])
        user = User(user_name="Sk", user_id="123")
        user.save()
        user = User.objects.get(user_id="123")
        user.save()
        new_entry = OffenceLog(user=user, offence_type="on_leave")
        new_entry.save()
        resp = self.client.get('/slack/leaderboard/?q=weekly')
        self.assertJSONEqual((resp.content), [{u'name': 'Sk', u'on_leave': 1,
                                               u'arrive_late': 0,
                                               u'leave_early': 0}])
        content = json.loads(resp.content)
        self.assertEqual(content[0], {u'name': 'Sk', u'on_leave': 1,
                                      u'arrive_late': 0,
                                      u'leave_early': 0})
        resp = self.client.get('/slack/leaderboard/?q=monthly')
        self.assertJSONEqual((resp.content), [{u'name': 'Sk', u'on_leave': 1,
                                               u'arrive_late': 0,
                                               u'leave_early': 0}])
        content = json.loads(resp.content)
        self.assertEqual(content[0], {u'name': 'Sk', u'on_leave': 1,
                                      u'arrive_late': 0,
                                      u'leave_early': 0})
