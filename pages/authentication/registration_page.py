from playwright.sync_api import Page
import re
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.login_link = Link(page, 'registration-page-login-link', 'Login link')

    def click_login_link(self):
        """Переход по ссылке входа"""
        self.login_link.click()
        self.check_current_url(re.compile(".*/#/auth/login"))

    def click_registration_button(self):
        """Нажатие кнопки регистрации"""
        self.registration_form.click_registration_button()