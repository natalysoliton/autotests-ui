from playwright.sync_api import Page
import re
from components.authentication.login_form_component import LoginFormComponent
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        self.registration_link = Link(page, 'login-page-registration-link', 'Registration link')
        self.wrong_email_or_password_alert = Text(
            page,
            'login-page-wrong-email-or-password-alert',
            'Wrong email or password alert'
        )

    def click_registration_link(self):
        """Переход по ссылке регистрации"""
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))

    def check_visible_wrong_email_or_password_alert(self):
        """Проверка отображения алерта об ошибке авторизации"""
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text('Wrong email or password')