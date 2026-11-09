from django.test import TestCase
from django.contrib.auth.models import User


class LogoutTests(TestCase):
    def test_logout_post_ends_session_and_redirects_to_login(self):
        user = User.objects.create_user(username='logout-test', password='test-password')
        self.client.force_login(user)

        response = self.client.post('/logout/')

        self.assertRedirects(response, '/login/')
        self.assertNotIn('_auth_user_id', self.client.session)
