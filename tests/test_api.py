import os
from unittest import TestCase

import version
import webapp.main


class TestWebApp(TestCase):
    def setUp(self):
        os.environ['DEBUG'] = 'true'
        os.environ['ENV_GIT_COMMIT_SHA'] = 'xxxyyyzzz'
        self.app = webapp.main.app.test_client()

    def test_root_alive(self):
        r = self.app.get('/', follow_redirects=True)
        self.assertEqual(r.status_code, 200)

    def test_healthcheck_alive(self):
        r = self.app.get('/healthcheck', follow_redirects=True)
        self.assertEqual(r.status_code, 200, 'Root URL must return 200')

    def test_healthcheck_content(self):
        r = self.app.get('/healthcheck', follow_redirects=True)
        j = r.get_json()
        self.assertIn('description', j, 'healthcheck must contain description')
        self.assertIn('sha', j, 'healthcheck must contain sha')
        self.assertIn('version', j, 'healthcheck must contain version')
        self.assertEqual(j['description'], 'Tech test 2', 'description must be Tech test 2')
        self.assertEqual(j['sha'], 'xxxyyyzzz', 'sha must be xxxyyyzzz')
        self.assertEqual(j['version'], version.version, f'version must be {version.version}')
