from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from ..views import signup


class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def setUp(self):
            url = reverse('signup')
            self.response = self.client.get(url)

    def test_signup_status_code(self):
            self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
            view = resolve('/signup/')
            self.assertEquals(view.func, signup)

    def test_csrf(self):
            self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
            form = self.response.context.get('form')
            self.assertIsInstance(form, UserCreationForm)

    def test_input_form(self):
        '''
                The view must contain five inputs: csrf, username, email,
                password1, password2
                '''
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)