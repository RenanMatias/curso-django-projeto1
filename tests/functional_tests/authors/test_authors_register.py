import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsRegisterTest(AuthorsBaseTest):

    def fill_form_dummy_data(self, form):
        fields = form.find_elements(By.TAG_NAME, 'input')

        for field in fields:
            if field.is_displayed():
                field.send_keys(' '*20)

    def get_form(self):
        return self.browser.find_element(
            By.XPATH,
            '/html/body/main/div[2]/form'
        )

    def form_field_test_with_callback(self, callback):
        self.browser.get(self.live_server_url + '/authors/register/')

        form = self.get_form()

        self.fill_form_dummy_data(form)
        form.find_element(By.NAME, 'email').send_keys('email@email.com')

        callback(form)
        return form

    def test_empty_first_name_error_message(self):

        def callback(form):
            first_name_field = form.find_element(By.NAME, 'first_name')
            first_name_field.send_keys(' ')
            first_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your first name', form.text)

        self.form_field_test_with_callback(callback)

    def test_empty_last_name_error_message(self):

        def callback(form):
            last_name_field = form.find_element(By.NAME, 'last_name')
            last_name_field.send_keys(' ')
            last_name_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Write your last name', form.text)

        self.form_field_test_with_callback(callback)

    def test_empty_username_error_message(self):

        def callback(form):
            username_field = form.find_element(By.NAME, 'username')
            username_field.send_keys(' ')
            username_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('This field must not be empty', form.text)

        self.form_field_test_with_callback(callback)

    def test_invalid_email_error_message(self):

        def callback(form):
            email_field = form.find_element(By.NAME, 'email')
            email_field.send_keys('email@invalid')
            email_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('The email must be valid.', form.text)

        self.form_field_test_with_callback(callback)

    def test_invalid_password_error_message(self):

        def callback(form):
            password_field = form.find_element(By.NAME, 'password')
            password_field.send_keys(' ')
            password_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Password must not be empty.', form.text)

        self.form_field_test_with_callback(callback)

    def test_passwords_do_not_mach(self):

        def callback(form):
            password_field = form.find_element(By.NAME, 'password')
            password2_field = form.find_element(By.NAME, 'password2')
            password_field.send_keys('P@ssw0rd')
            password2_field.send_keys('P@ssw0rd_Different')
            password2_field.send_keys(Keys.ENTER)
            form = self.get_form()
            self.assertIn('Password and password2 must be equal', form.text)

        self.form_field_test_with_callback(callback)

    def test_user_valid_data_register_successfully(self):
        self.browser.get(self.live_server_url + '/authors/register/')
        form = self.get_form()

        form.find_element(By.NAME, 'first_name').send_keys('First Name')
        form.find_element(By.NAME, 'last_name').send_keys('Last Name')
        form.find_element(By.NAME, 'username').send_keys('my_username')
        form.find_element(By.NAME, 'email').send_keys('email@valid.com')
        form.find_element(By.NAME, 'password').send_keys('P@ssw0rd')
        form.find_element(By.NAME, 'password2').send_keys('P@ssw0rd')

        form.submit()

        self.assertIn('Your user is created, please log in.',
                      self.browser.find_element(By.TAG_NAME, 'body').text)
