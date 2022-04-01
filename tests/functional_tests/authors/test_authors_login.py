import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By

from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = 'pass'
        user = User.objects.create_user(
            username='my_user', password=string_password)

        # User opens the login page
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # User sees the login form
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.browser.find_element(By.NAME, 'username')
        password_field = self.browser.find_element(By.NAME, 'password')

        # User types your username and password
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # User clicks the login button
        form.submit()

        # User sees the message that successfully logged and their name
        self.assertIn(
            f'You are logged in with {user.username}.',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
